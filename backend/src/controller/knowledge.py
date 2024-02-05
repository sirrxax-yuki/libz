from api.schemas.user import User as UserSchema
from api.schemas.knowledge import Knowledge, KnowledgeMapping
from controller.user import User
from models.database.knowledge import KnowledgeDatabaseAccessor
from models.exception import UserInactiveException
from settings import DEBUG_MODE
from logs import logger
from time import time


class KnowledgeController:

    # Note.
    # If validation maybe bottleneck, change to validate user only at login.
    
    def insert_knowledge(
        self,
        user: UserSchema,
        keywords: list[str],
        knowledge: str,
        knowledge_type: str = 'text',
        is_private: bool = False,
    ) -> int:
        with self.create_database_accessor() as database:
            user_id = self.validate_user(database, user)
            return database.insert_knowledge(user_id, keywords, knowledge, knowledge_type, is_private)

    def fetch_knowledge(self, user: UserSchema, keyword: str) -> list[dict]:
        with self.create_database_accessor() as database:
            user_id = self.validate_user(database, user)
            return database.fetch_knowledge_list(user_id, keyword)

    def listup_knowledge(self, user: UserSchema) -> list[KnowledgeMapping]:
        with self.create_database_accessor() as database:
            user_id = self.validate_user(database, user)
            return self.convert_knowledge_mapping(
                database.fetch_knowledge_mappings(user_id)
            )

    def delete_knowledge(self, user: UserSchema, knowledge_id: int) -> list[KnowledgeMapping]:
        with self.create_database_accessor() as database:
            user_id = self.validate_user(database, user)
            return self.convert_knowledge_mapping(
                database.delete_knowledge_and_fetch_knowledge_mappings(user_id, knowledge_id)
            )
    
    def create_database_accessor(self) -> KnowledgeDatabaseAccessor:
        return KnowledgeDatabaseAccessor()

    def convert_knowledge_mapping(self, source: list[dict]) -> list[KnowledgeMapping]:
        return [
            KnowledgeMapping(
                keywords=s['keywords'],
                knowledge=Knowledge(
                    knowledge_id=s['knowledge']['knowledge_id'],
                    type=s['knowledge']['type'],
                    contents=s['knowledge']['contents'],
                    private=s['knowledge']['private'],
                    user_id=s['knowledge']['user_id'],
                    user_name=s['knowledge']['user_name'],
                ),
            )
            for s in source
        ]

    def validate_user(self, database, user_schema: UserSchema) -> str:
        if DEBUG_MODE:
            database.upsert_user('debug.user', 'DEBUG', '9999999999')
            return 'debug.user'
        user = User(user_schema)
        if not user.is_active:
            raise UserInactiveException
        start = time()
        database.upsert_user(user.user_id, user.user_name, user.tenant_id)
        logger.info(f"upsert_user: {round(time() - start, 3)} sec.")
        return user.user_id
    