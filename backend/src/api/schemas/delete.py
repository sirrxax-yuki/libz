from pydantic import BaseModel, Field

from .user import User
from .knowledge import KnowledgeMapping


class DeleteKnowledgeRequest(BaseModel):
    user: User = Field(User(), description="Operator info.")
    knowledge_id: int = Field(0, description="Delete target knowledge ID.")

class DeleteKnowledgeResponse(BaseModel):
    update: list[KnowledgeMapping] = Field([], description="Updated list of keywords and knowledge for delete operation.")
