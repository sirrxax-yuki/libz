from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import Boolean, DateTime, Integer, String, Text

from models.database.dto import Base, to_dict, to_string


class Keyword(Base):
    __tablename__ = 'keyword'
    
    keyword_id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(Text, nullable=False)
    knowledge_id = Column(
        Integer,
        ForeignKey('knowledge.knowledge_id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
    )
    create_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        default=current_timestamp(),
    )
    update_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        default=current_timestamp(),
        onupdate=current_timestamp(),
    )

    def __repr__(self) -> str:
        return to_string(self)
    
    def to_dict(self) -> dict[str, str]:
        return to_dict(self)


class Knowledge(Base):
    __tablename__ = 'knowledge'
    
    knowledge_id = Column(Integer, autoincrement=True, primary_key=True)
    type_id = Column(
        String(8),
        ForeignKey('knowledge_type.knowledge_type_id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
    )
    contents = Column(Text, nullable=False)
    private = Column(Boolean, nullable=False)
    user_id = Column(
        String(36),
        ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
    )
    create_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        default=current_timestamp(),
    )
    update_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        default=current_timestamp(),
        onupdate=current_timestamp(),
    )

    relation_favorite = relationship('Favorite')
    relation_keyword = relationship('Keyword')

    def __repr__(self) -> str:
        return to_string(self)
    
    def to_dict(self) -> dict[str, str]:
        return to_dict(self)


class KnowledgeType(Base):
    # Master table
    __tablename__ = 'knowledge_type'
    
    knowledge_type_id = Column(String(8), primary_key=True)
    create_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        default=current_timestamp(),
    )
    update_datetime = Column(
        DateTime(timezone=True),
        nullable=False,
        default=current_timestamp(),
        onupdate=current_timestamp(),
    )

    relation_knowledge = relationship('Knowledge')

    def __repr__(self) -> str:
        return to_string(self)
    
    def to_dict(self) -> dict[str, str]:
        return to_dict(self)
