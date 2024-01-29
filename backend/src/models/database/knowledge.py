from models.database import DatabaseAccessor
from models.database.dto.attribute import Favorite
from models.database.dto.knowledge import Keyword, Knowledge, KnowledgeType
from models.database.dto.user import User
from models.database.dto.tenant import Tenant
from models.database.mixin.initialize_operation import InitializeOperation
from models.database.mixin.knowledge_delete_operation import KnowledgeDeleteOperation
from models.database.mixin.knowledge_fetch_operation import KnowledgeFetchOperation
from models.database.mixin.knowledge_upsert_operation import KnowledgeUpsertOperation
from models.database.mixin.user_upsert_operation import UserUpsertOperation
from settings import DATABASE_URL


class KnowledgeDatabaseAccessor(
    DatabaseAccessor,
    UserUpsertOperation,
    KnowledgeFetchOperation,
    KnowledgeUpsertOperation,
    KnowledgeDeleteOperation,
):

    def __init__(self):
        super().__init__(DATABASE_URL)
    
    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, traceback):
        self.connection.close()
    
    def __del__(self):
        self.engine.dispose()


class KnowledgeDatabaseInitializer(
    DatabaseAccessor,
    InitializeOperation,
    UserUpsertOperation,
    KnowledgeUpsertOperation,
    KnowledgeDeleteOperation,
):

    def __init__(self):
        super().__init__(DATABASE_URL)
    
    def __enter__(self):
        return self
    
    def __exit__(self, ex_type, ex_value, traceback):
        self.connection.close()
    
    def __del__(self):
        self.engine.dispose()
