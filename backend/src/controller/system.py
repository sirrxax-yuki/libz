from models.database.knowledge import KnowledgeDatabaseInitializer


class SystemController:

    def initialize_all_tables(self):
        with self.create_database_accessor() as database:
            database.create_all_tables()
            database.initialize_master_tables()

    def drop_all_tables(self):
        with self.create_database_accessor() as database:
            database.drop_all_tables()
    
    def insert_knowledges(
        self,
        user_id: str,
        user_name: str,
        tenant_id: str,
        knowledges: list[dict],
    ):
        with self.create_database_accessor() as database:
            database.upsert_user(user_id, user_name, tenant_id)
            database.insert_knowledges(user_id, knowledges)
    
    def create_database_accessor(self) -> KnowledgeDatabaseInitializer:
        return KnowledgeDatabaseInitializer()
