from sqlalchemy import Column, SmallInteger, BigInteger, VARCHAR, DECIMAL, ForeignKey, \
    Boolean, Integer, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'
    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    is_published = Column(Boolean, nullable=False)
    name = Column(VARCHAR(20), nullable=False)


class Product(Base):
    __tablename__: str = "products"
    id = Column(Integer, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    total = Column(Integer, nullable=False)
    is_published = Column(Boolean, nullable=False)
    name = Column(VARCHAR(20), nullable=False)


class Language(Base):
    __tablename__: str = "languages"
    id = Column(SmallInteger, primary_key=True)
    language_code = Column(VARCHAR(2), nullable=False)


class Status(Base):
    __tablename__: str = "statuses"
    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(7), nullable=False)


class User(Base):
    __tablename__: str = "users"
    id = Column(BigInteger, primary_key=True)
    is_blocked = Column(Boolean, nullable=False)
    balance = Column(DECIMAL(8, 2), nullable=False)
    language_id = Column(SmallInteger, ForeignKey('languages.id'), nullable=False)


class Invoice(Base):
    __tablename__: str = "invoices"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    date_created = Column(DateTime, nullable=False)
    total = Column(SmallInteger, nullable=False)
    status_id = Column(SmallInteger, ForeignKey('statuses.id'), nullable=False)


class Order(Base):
    __tablename__: str = "orders"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    date_created = Column(DateTime, nullable=False)
    status_id = Column(SmallInteger, ForeignKey('statuses.id'), nullable=False)
    invoice_id = Column(BigInteger, ForeignKey('invoices.id'), nullable=False)


class OrderItem(Base):
    __tablename__: str = "order_items"
    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    total = Column(Integer, nullable=False)






