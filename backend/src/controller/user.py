from api.schemas.user import User as UserSchema

class User:

    def __init__(self, user: UserSchema):
        self.__user_id = user.data.ext.userId
        self.__user_name = f"{user.data.family_name} {user.data.given_name}"
        self.__tenant_id = user.data.ext.tenantId
        self.__status = user.data.ext.status
    
    @property
    def user_id(self) -> str:
        return self.__user_id
    
    @property
    def user_name(self) -> str:
        return self.__user_name
    
    @property
    def tenant_id(self) -> str:
        return self.__tenant_id

    @property
    def is_active(self) -> bool:
        return self.__status == 'active'
