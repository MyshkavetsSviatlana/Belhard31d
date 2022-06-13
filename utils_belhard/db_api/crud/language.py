from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from utils_belhard.db_api.engine import create_session
from utils_belhard.db_api.models import Language


class LanguageCrud(object):

    @staticmethod
    @create_session
    def add(language_code: str, session: Session = None) -> Language:
        language = Language(language_code=language_code)
        session.add(language)
        session.commit()
        session.refresh(language)
        return language

    @staticmethod
    @create_session
    def get(language_id: int, session: Session = None) -> Language | None:
        # return session.get(Language, language_id)
        language = session.execute(
            select(Language).where(Language.id == language_id)
        )
        if language := language.first():
            return language[0]

    @staticmethod
    @create_session
    def delete(language_id: int, session: Session = None) -> None:
        session.execute(
            delete(Language).where(Language.id == language_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(language_id: int, language_code: str, session: Session = None) -> None:
        session.execute(
            update(Language).where(Language.id == language_id).values(
                language_code=language_code if language_code else Language.language_code
            )
        )
        session.commit()
