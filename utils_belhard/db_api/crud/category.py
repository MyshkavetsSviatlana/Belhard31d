from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from utils_belhard.db_api.engine import create_session
from utils_belhard.db_api.models import Category


class CategoryCrud(object):

    @staticmethod
    @create_session
    def add(parent_id: int = None, is_published: bool = False, name: str = None,
            session: Session = None) -> Category:
        category = Category(
            parent_id=parent_id,
            is_published=is_published,
            name=name
        )
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> Category | None:
        # return session.get(Category, category_id)
        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        # try:
        #     return category.first()[0]
        # except TypeError:
        #     return None

        if category := category.first():
            return category[0]

    @staticmethod
    @create_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category).where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(category_id: int, parent_id: int = None, is_published: bool = False, name: str = None,
               session: Session = None) -> None:
        session.execute(
            update(Category).where(Category.id == category_id).values(
                is_published=is_published if is_published else Category.is_published,
                parent_id=parent_id if parent_id else Category.parent_id,
                name=name if name else Category.name
            )
        )
        session.commit()
