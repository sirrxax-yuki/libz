from pydantic import BaseModel, Field

from .knowledge import Knowledge
from .user import User


class SearchKnowledgeRequest(BaseModel):
    user: User = Field(User(), description="Operator info.")
    keyword: str = Field('', description="Keyword for search.")

class SearchKnowledgeResponse(BaseModel):
    results: list[Knowledge] = Field([], description="List of knowledge with user info.")
