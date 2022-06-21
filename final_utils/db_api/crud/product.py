from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from final_utils.db_api.engine import create_session
from final_utils.db_api.models import Product


class ProductCrud(object):

    @staticmethod
    @create_session
    async def add(category_id: int, name: str, page: int, position: int, session: AsyncSession = None) -> Product:
        product = Product(
            category_id=category_id,
            name=name,
            page=page,
            position=position
        )
        session.add(product)
        await session.commit()
        await session.refresh(product)
        return product

    @staticmethod
    @create_session
    def get(product_id: int, session: AsyncSession = None) -> Product | None:
        product = await session.execute(
            select(Product).where(Product.id == product_id)
        )
        if product := product.first():
            return product[0]

    @staticmethod
    @create_session
    async def delete(product_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Product).where(Product.id == product_id)
        )
        await session.commit()

    @staticmethod
    @create_session
    async def update(product_id: int, category_id: int, name: str, page: int, position: int,
               session: AsyncSession = None) -> None:
        await session.execute(
            update(Product).where(Product.id == product_id).values(
                category_id=category_id if category_id else Product.category_id,
                name=name if name else Product.name,
                page=page if page else Product.page,
                position=position if position else Product.position
            )
        )
        await session.commit()
