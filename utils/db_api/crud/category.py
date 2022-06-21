from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from utils.db_api.engine import create_session
from utils.db_api.models import Category


class CategoryCrud(object):

    @staticmethod
    @create_session
    async def add(name: str, parent_id: int = None, session: AsyncSession = None) -> Category:
        category = Category(
            name=name,
            parent_id=parent_id
        )
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category

    @staticmethod
    @create_session
    async def get(category_id: int, session: AsyncSession = None) -> Category | None:
        # return session.get(Category, category_id)
        category = await session.execute(
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
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Category).where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_session
    async def update(category_id: int, name: str, parent_id: int = None,
                     session: AsyncSession = None) -> None:
        await session.execute(
            update(Category).where(Category.id == category_id).values(
                name=name if name else Category.name,
                parent_id=parent_id if parent_id else Category.parent_id
            )
        )
        await session.commit()
