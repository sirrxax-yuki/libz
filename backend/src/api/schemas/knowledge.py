from pydantic import BaseModel, Field


class Knowledge(BaseModel):
    knowledge_id: int = Field(0, description="Knowledge ID.")
    type: str = Field('', description="Knowledge type. (ex. text)")
    contents: str = Field('', description="Knowledge text.")
    private: bool = Field(False, description="Knowledge's visibility.")
    user_id: str = Field('', description="Posted user ID.")
    user_name: str = Field('', description="Posted user name.")

class KnowledgeMapping(BaseModel):
    keywords: list[str] = Field([], description="Keyword list.")
    knowledge: Knowledge = Field(Knowledge(), description="Knowledge.")
