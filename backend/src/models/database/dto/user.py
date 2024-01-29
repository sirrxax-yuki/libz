from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import DateTime, String, Text

from models.database.dto import Base, to_dict, to_string


class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(36), primary_key=True)
    user_name = Column(Text, nullable=False)
    tenant_id = Column(
        String(36),
        ForeignKey('tenant.tenant_id', onupdate='CASCADE', ondelete='CASCADE'),
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
    relation_knowledge = relationship('Knowledge')

    def __repr__(self) -> str:
        return to_string(self)
    
    def to_dict(self) -> dict[str, str]:
        return to_dict(self)
