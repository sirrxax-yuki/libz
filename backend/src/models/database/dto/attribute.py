from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import DateTime, Integer, String, Text

from models.database.dto import Base, to_dict, to_string


class Favorite(Base):
    __tablename__ = 'favorite'
    
    favorite_id = Column(Integer, autoincrement=True, primary_key=True)
    comment = Column(Text, nullable=False)
    user_id = Column(
        String(36),
        ForeignKey('user.user_id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False,
    )
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
