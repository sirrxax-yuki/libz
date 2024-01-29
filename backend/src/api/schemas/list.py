from pydantic import BaseModel, Field

from .user import User
from .knowledge import KnowledgeMapping


class ListKnowledgeRequest(BaseModel):
    user: User = Field(User(), description="Operator info.")

class ListKnowledgeResponse(BaseModel):
    results: list[KnowledgeMapping] = Field([], description="Updated list of keywords and knowledge.")
