from models.database.dto import Base
from models.database.dto.knowledge import KnowledgeType


class InitializeOperation:

    def create_all_tables(self):
        Base.metadata.create_all(bind=self.engine)
        self.commit()

    def drop_all_tables(self):
        Base.metadata.drop_all(bind=self.engine)
        self.commit()
    
    def initialize_master_tables(self):
        with self.create_session() as session:
            try:
                self.truncate_knowledge_type_in_session(session)
                self.initialize_knowledge_type_in_session(session)
                session.commit()
            except Exception:
                session.rollback()
                raise

    def truncate_master_tables(self):
        with self.create_session() as session:
            try:
                self.truncate_knowledge_type_in_session(session)
                session.commit()
            except Exception:
                session.rollback()
                raise

    def initialize_knowledge_type(self):
        with self.create_session() as session:
            try:
                self.truncate_knowledge_type_in_session(session)
                self.initialize_knowledge_type_in_session(session)
                session.commit()
            except Exception:
                session.rollback()
                raise

    def truncate_knowledge_type(self):
        with self.create_session() as session:
            try:
                self.truncate_knowledge_type_in_session(session)
                session.commit()
            except Exception:
                session.rollback()
                raise
    
    def initialize_knowledge_type_in_session(self, session):
        knowledge_types = [ 'text', 'image' ]
        session.add_all([
            KnowledgeType(knowledge_type_id=t) for t in knowledge_types
        ])
        session.flush()

    def truncate_knowledge_type_in_session(self, session):
        session.query(KnowledgeType).delete()
        session.flush()
