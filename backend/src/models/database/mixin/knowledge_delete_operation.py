from sqlalchemy import and_

from models.database.dto.knowledge import Knowledge


class KnowledgeDeleteOperation:
    
    def delete_knowledge(self, user_id: str, knowledge_id: int):
        with self.create_session() as session:
            try:
                self.delete_knowledge_in_session(session, user_id, knowledge_id)
                session.commit()
            except BaseException:
                session.rollback()
                raise
    
    def delete_knowledge_and_fetch_knowledge_mappings(self, user_id: str, knowledge_id: int) -> list[dict]:
        with self.create_session() as session:
            try:
                self.delete_knowledge_in_session(session, user_id, knowledge_id)
                session.commit()
                return self.fetch_knowledge_mappings_in_session(session, user_id)
            except BaseException:
                session.rollback()
                raise

    def delete_knowledge_in_session(self, session, user_id: str, knowledge_id: int):
        session.query(Knowledge).filter(
            and_(
                Knowledge.knowledge_id == knowledge_id,
                Knowledge.user_id == user_id,
            )
        ).delete()
        session.flush()
