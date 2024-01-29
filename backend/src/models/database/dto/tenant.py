from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import DateTime, String

from models.database.dto import Base, to_dict, to_string


class Tenant(Base):
    __tablename__ = 'tenant'

    tenant_id = Column(String(36), primary_key=True)
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

    relation_user = relationship('User')

    def __repr__(self) -> str:
        return to_string(self)
    
    def to_dict(self) -> dict[str, str]:
        return to_dict(self)
    