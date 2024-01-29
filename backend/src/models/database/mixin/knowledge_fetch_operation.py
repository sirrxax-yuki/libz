from sqlalchemy import and_, or_

from models.database.exception import KnowledgeNotFoundException
from models.database.dto.knowledge import Keyword, Knowledge
from models.database.dto.user import User


class KnowledgeFetchOperation:

    def fetch_knowledge(self, user_id: str, knowledge_id: int) -> dict:
        with self.create_session() as session:
            knowledge_info = session.query(Knowledge).filter(
                and_(
                    Knowledge.knowledge_id == knowledge_id,
                    Knowledge.user_id == user_id,
                )
            ).one_or_none()
            if not knowledge_info:
                raise KnowledgeNotFoundException
            return knowledge_info.to_dict()

    def fetch_knowledge_list(self, user_id: str, keyword: str) -> list[dict]:
        with self.create_session() as session:
            keyword_records = session.query(Keyword).filter(
                Keyword.text == keyword,
            )
            knowledge_all_records = session.query(
                Knowledge,
                Knowledge.knowledge_id,
                Knowledge.type_id,
                Knowledge.contents,
                Knowledge.private,
                Knowledge.user_id,
                User.user_name,
                Knowledge.create_datetime,
                Knowledge.update_datetime,
            ).join(
                User,
                User.user_id == Knowledge.user_id,
            )
            knowledge_records_joined = []
            for keyword in keyword_records.all():
                knowledge_records_joined.extend([
                    r for r in knowledge_all_records.filter(
                        and_(
                            Knowledge.knowledge_id == keyword.knowledge_id,
                            or_(
                                Knowledge.user_id == user_id,
                                and_(
                                    Knowledge.user_id != user_id,
                                    Knowledge.private == False,
                                )
                            )
                        )
                    ).order_by(
                        Knowledge.update_datetime.desc(),
                        Knowledge.knowledge_id.desc(),
                    ).all()
                ])
            return [
                self.convert_to_knowledge_schema(r)
                for r in sorted(
                    knowledge_records_joined,
                    key=lambda r: 0 if r.user_id == user_id else 1,
                )
            ]
    
    def fetch_knowledge_keyword_list(self, user_id: str, knowledge_id: int) -> list[dict]:
        with self.create_session() as session:
            keywords = session.query(Keyword).join(
                Knowledge,
                Knowledge.knowledge_id == Keyword.knowledge_id,
            ).filter(
                and_(
                    Keyword.knowledge_id == knowledge_id,
                    Knowledge.user_id == user_id,
                )
            ).order_by(
                Knowledge.update_datetime.desc(),
                Knowledge.knowledge_id.desc(),
            ).all()
            return [ k.to_dict() for k in keywords ]

    def fetch_knowledge_mappings(self, user_id: str) -> list[dict]:
        with self.create_session() as session:
            return self.fetch_knowledge_mappings_in_session(session, user_id)

    def fetch_knowledge_mappings_in_session(self, session, user_id: str) -> list[dict]:
        return [
            {
                'keywords': self.fetch_keyword_texts_in_session(session, knowledge.knowledge_id),
                'knowledge': self.convert_to_knowledge_schema(knowledge),
            }
            for knowledge in self.fetch_knowledges_in_session(session, user_id)
        ]
    
    def fetch_knowledges_in_session(self, session, user_id: str) -> list:
        return session.query(
            Knowledge,
            Knowledge.knowledge_id,
            Knowledge.type_id,
            Knowledge.contents,
            Knowledge.private,
            Knowledge.user_id,
            User.user_name,
            Knowledge.create_datetime,
            Knowledge.update_datetime,
        ).join(
            User,
            User.user_id == Knowledge.user_id,
        ).filter(
            Knowledge.user_id == user_id,
        ).order_by(
            Knowledge.update_datetime.desc(),
            Knowledge.knowledge_id.desc(),
        ).all()

    def fetch_keyword_texts_in_session(self, session, knowledge_id: int) -> list[str]:
        return [
            k.text for k in session.query(Keyword).filter(
                Keyword.knowledge_id == knowledge_id,
            ).all()
        ]

    def convert_to_knowledge_schema(self, knowledge) -> dict:
        return {
            'knowledge_id': knowledge.knowledge_id,
            'type': knowledge.type_id,
            'contents': knowledge.contents,
            'private': knowledge.private,
            'user_id': knowledge.user_id,
            'user_name': knowledge.user_name,
        }
