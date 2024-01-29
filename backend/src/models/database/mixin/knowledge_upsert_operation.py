from models.database.dto.knowledge import Keyword, Knowledge


class KnowledgeUpsertOperation:

    def insert_knowledge(
        self,
        user_id: str,
        keywords: list[str],
        knowledge: str,
        knowledge_type: str = 'text',
        is_private: bool = False,
    ) -> int:
        with self.create_session() as session:
            try:
                knowledge_id = self.insert_knowledge_in_session(
                    session,
                    user_id,
                    knowledge,
                    knowledge_type,
                    is_private,
                )
                self.insert_keywords_in_session(session, knowledge_id, keywords)
                session.commit()
                return knowledge_id
            except Exception:
                session.rollback()
                raise

    def insert_knowledges(
        self,
        user_id: str,
        knowledge_mappings: list[dict],
    ):
        with self.create_session() as session:
            try:
                for m in knowledge_mappings:
                    knowledge_id = self.insert_knowledge_in_session(
                        session,
                        user_id,
                        m['knowledge'],
                        m['type'],
                        m['private'],
                    )
                    self.insert_keywords_in_session(session, knowledge_id, m['keywords'])
                session.commit()
            except Exception:
                session.rollback()
                raise
    
    def insert_knowledge_in_session(
        self,
        session,
        user_id: str,
        knowledge: str,
        knowledge_type: str = 'text',
        is_private: bool = False,
    ) -> int:
        knowledge = Knowledge(
            type_id=knowledge_type,
            contents=knowledge,
            private=is_private,
            user_id=user_id,
        )
        session.add(knowledge)
        session.flush()
        return knowledge.knowledge_id

    def insert_keywords_in_session(self, session, knowledge_id: int, keywords: list[str]):
        session.add_all([
            Keyword(text=k, knowledge_id=knowledge_id) for k in keywords
        ])
        session.flush()
