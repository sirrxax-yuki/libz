from pydantic import BaseModel, Field

from .rsi.user import RSIUser


class User(BaseModel):
    data: RSIUser = Field(RSIUser(), description="User info.")
