from models.error import (
    CODE_TENANT_NOT_FOUND,
    MESSAGE_TENANT_NOT_FOUND,
    CODE_USER_NOT_FOUND,
    MESSAGE_USER_NOT_FOUND,
    CODE_KNOWLEDGE_NOT_FOUND,
    MESSAGE_KNOWLEDGE_NOT_FOUND,
)
from models.exception import LibzException


class TenantNotFoundException(LibzException):
    def __init__(self):
        super().__init__(code=CODE_TENANT_NOT_FOUND, message=MESSAGE_TENANT_NOT_FOUND, status=403)

class UserNotFoundException(LibzException):
    def __init__(self):
        super().__init__(code=CODE_USER_NOT_FOUND, message=MESSAGE_USER_NOT_FOUND, status=403)

class KnowledgeNotFoundException(LibzException):
    def __init__(self):
        super().__init__(code=CODE_KNOWLEDGE_NOT_FOUND, message=MESSAGE_KNOWLEDGE_NOT_FOUND, status=404)
