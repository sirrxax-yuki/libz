from pydantic import BaseModel, Field

from .user import User


class PostKnowledgeRequest(BaseModel):
    user: User = Field(User(), description="Operator info.")
    keywords: list[str] = Field([], description="Keywords for knowledge.")
    knowledge: str = Field('', description="Knowledge text.")
    knowledge_type: str = Field('text', description="Knowledge type.")
    private: bool = Field(False, description="Knowledge is hidden to another users.")

class PostKnowledgeResponse(BaseModel):
    knowledge_id: int = Field(0, description="Posted knowledge ID.")
