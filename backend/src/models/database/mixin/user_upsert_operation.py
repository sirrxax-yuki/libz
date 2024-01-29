from sqlalchemy import and_

from models.database.dto.tenant import Tenant
from models.database.dto.user import User


class UserUpsertOperation:

    def upsert_tenant(self, tenant_id: str):
        with self.create_session() as session:
            try:
                self.upsert_tenant_in_session(session, tenant_id)
                session.commit()
            except Exception:
                session.rollback()
                raise
    
    def upsert_user(self, user_id: str, user_name: str, tenant_id: str):
        with self.create_session() as session:
            try:
                self.upsert_tenant_in_session(session, tenant_id)
                self.upsert_user_in_session(session, user_id, user_name, tenant_id)
                session.commit()
            except Exception:
                session.rollback()
                raise
    
    def upsert_user_in_session(self, session, user_id: str, user_name: str, tenant_id: str):
        user = session.query(User).filter(
            and_(
                User.user_id == user_id,
                User.tenant_id == tenant_id,
            )
        ).one_or_none()
        if user:
            user.user_name = user_name
        else:
            session.add(User(
                user_id=user_id,
                user_name=user_name,
                tenant_id=tenant_id,
            ))
        session.flush()

    def upsert_tenant_in_session(self, session, tenant_id: str):
        tenant = session.query(Tenant).filter(
            Tenant.tenant_id == tenant_id,
        ).one_or_none()
        if not tenant:
            session.add(Tenant(
                tenant_id=tenant_id,
            ))
        session.flush()
