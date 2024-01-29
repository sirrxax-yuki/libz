from sqlalchemy import and_

from models.database.dto.tenant import Tenant
from models.database.dto.user import User
from models.database.exception import TenantNotFoundException, UserNotFoundException


class UserFetchOperation:

    def fetch_user(self, user_id: str, tenant_id: str) -> dict:
        with self.create_session() as session:
            return self.fetch_user_in_session(session, user_id, tenant_id)

    def fetch_user_list(self) -> list[dict]:
        with self.create_session() as session:
            self.fetch_user_list_in_session(session)

    def fetch_tenant(self, tenant_id: str) -> dict:
        with self.create_session() as session:
            return self.fetch_tenant_in_session(session, tenant_id)
    
    def fetch_user_in_session(self, session, user_id: str, tenant_id: str) -> dict:
        user = session.query(User).filter(
            and_(
                User.user_id == user_id,
                User.tenant_id == tenant_id,
            )
        ).one_or_none()
        if not user:
            raise UserNotFoundException
        return user.to_dict()

    def fetch_user_list_in_session(self, session) -> list[dict]:
        users = session.query(User).all()
        return [ u.to_dict() for u in users ]

    def fetch_tenant_in_session(self, session, tenant_id: str) -> list[dict]:
        tenant = session.query(Tenant).filter(
            Tenant.tenant_id == tenant_id,
        ).one_or_none()
        if not tenant:
            raise TenantNotFoundException
        return tenant.to_dict()
