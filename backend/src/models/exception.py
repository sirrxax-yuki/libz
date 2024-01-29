from models.error import (
    CODE_USER_INACTIVE,
    MESSAGE_USER_INACTIVE,
    CODE_UNKNOWN,
    MESSAGE_UNKNOWN,
)

class LibzException(Exception):
    def __init__(self,
        status: int = 500,
        code: str = CODE_UNKNOWN,
        message: str = MESSAGE_UNKNOWN,
        e: BaseException = None
    ):
        if e:
            super().__init__(e)
        self.__status = status
        self.__code = code
        self.__message = message
    
    @property
    def status(self) -> str:
        return self.__status
    
    @property
    def code(self) -> str:
        return self.__code
    
    @property
    def message(self) -> str:
        return self.__message

class UserInactiveException(LibzException):
    def __init__(self):
        super().__init__(code=CODE_USER_INACTIVE, message=MESSAGE_USER_INACTIVE, status=403)
