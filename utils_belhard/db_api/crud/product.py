from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from utils_belhard.db_api.engine import create_session
from utils_belhard.db_api.models import Product


class ProductCrud(object):

    @staticmethod
    @create_session
    def add(category_id: int = None, price: float = 0, total: int = 0, is_published: bool = False,
            name: str = None, session: Session = None) -> Product:
        product = Product(
            category_id=category_id,
            price=price,
            total=total,
            is_published=is_published,
            name=name
        )
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    @staticmethod
    @create_session
    def get(product_id: int, session: Session = None) -> Product | None:
        # return session.get(Product, product_id)
        product = session.execute(
            select(Product).where(Product.id == product_id)
        )
        if product := product.first():
            return product[0]

    @staticmethod
    @create_session
    def delete(product_id: int, session: Session = None) -> None:
        session.execute(
            delete(Product).where(Product.id == product_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(product_id: int = None, category_id: int = None, price: float = 0, total: int = 0,
               is_published: bool = False, name: str = None, session: Session = None) -> None:
        session.execute(
            update(Product).where(Product.id == product_id).values(
                category_id=category_id if category_id else Product.category_id,
                price=price if price else Product.price,
                total=total if total else Product.total,
                is_published=is_published if is_published else Product.is_published,
                name=name if name else Product.name
            )
        )
        session.commit()