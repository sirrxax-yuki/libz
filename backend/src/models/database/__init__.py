from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema, DropSchema
from sqlalchemy_utils import create_database, database_exists


__all__ = [ 'DatabaseAccessor' ]


class DatabaseAccessor:

    def __init__(self, url: str):
        self.__engine = create_engine(
            url,
            echo=False,
            echo_pool=False,
            pool_pre_ping=True,
            pool_recycle=60,
            pool_size=100,
        )
        if not self.has_database():
            create_database(self.engine.url)
        self.__connection = self.__engine.connect()
        self.__inspector = inspect(self.__engine)
        self.__session_factory = sessionmaker(bind=self.__engine, autocommit=False, autoflush=False)

    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, traceback):
        if self.connection:
            self.connection.close()

    def __del__(self):
        if self.engine:
            self.engine.dispose()

    @property
    def engine(self):
        return self.__engine

    @property
    def inspector(self):
        return self.__inspector

    @property
    def connection(self):
        return self.__connection
    
    @property
    def session_factory(self):
        return self.__session_factory
    
    def initialize_schema(self, schema_name: str):
        if schema_name:
            if self.has_schema('public'):
                self.drop_schema('public')
            if not self.has_schema(schema_name):
                self.create_schema(schema_name)
            self.commit()
    
    def commit(self):
        self.connection.commit()

    def create_session(self):
        return self.SessionContext(self.session_factory())

    def create_schema(self, schema_name: str):
        self.connection.execute(CreateSchema(schema_name))
    
    def drop_schema(self, schema_name: str):
        self.connection.execute(DropSchema(schema_name))
    
    def has_database(self) -> bool:
        return database_exists(self.engine.url)

    def has_schema(self, schema_name: str) -> bool:
        return schema_name and self.inspector.has_schema(schema_name)
    
    class SessionContext:
        def __init__(self, session):
            self.__core = session

        def __enter__(self):
            return self.__core

        def __exit__(self, ex_type, ex_value, traceback):
            self.__core.flush()
            self.__core.commit()
            self.__core.close()
