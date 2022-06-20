from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from utils.db_api.engine import create_session
from utils.db_api.models import Product


class ProductCrud(object):

    @staticmethod
    @create_session
    def add(name: str, descr: str | None, price: float = 0, category_id: int = None,
            session: Session = None) -> Product:
        product = Product(
            name=name,
            descr=descr,
            price=price,
            category_id=category_id
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
    def update(product_id: int, name: str, descr: str | None, price: float, category_id: int = None,
               session: Session = None) -> None:
        session.execute(
            update(Product).where(Product.id == product_id).values(
                name=name if name else Product.name,
                descr=descr if descr else Product.descr,
                price=price if price else Product.price,
                category_id=category_id if category_id else Product.category_id
            )
        )
        session.commit()
