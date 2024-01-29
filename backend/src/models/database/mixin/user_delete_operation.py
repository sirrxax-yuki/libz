from sqlalchemy import and_

from models.database.dto.tenant import Tenant
from models.database.dto.user import User


class UserDeleteOperation:

    def delete_user(self, user_id: str, tenant_id: str):
        with self.create_session() as session:
            try:
                self.delete_user_in_session(session, user_id, tenant_id)
                session.commit()
            except Exception:
                session.rollback()
                raise

    def delete_tenant(self, tenant_id: str):
        with self.create_session() as session:
            try:
                self.delete_tenant_in_session(session, tenant_id)
                session.commit()
            except Exception:
                session.rollback()
                raise

    def delete_tenant_in_session(self, session, tenant_id: str) -> dict:
        session.query(Tenant).filter(
            Tenant.tenant_id == tenant_id,
        ).delete()
        session.flush()

    def delete_user_in_session(self, session, user_id: str, tenant_id: str) -> dict:
        session.query(User).filter(
            and_(
                User.user_id == user_id,
                User.tenant_id == tenant_id,
            )
        ).delete()
        session.flush()
