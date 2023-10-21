from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    id = Column(INTEGER, autoincrement=True, primary_key=True)


class Status(Base):
    __tablename__ = "statuses"

    name = Column(VARCHAR(10), nullable=False, unique=True)
    orders = relationship(argument="Order", back_populates="status")


class Order(Base):
    __tablename__ = "orders"

    user_id = Column(INTEGER, ForeignKey(column="users.id", ondelete="RESTRICT"), nullable=False, index=True)
    status_id = Column(INTEGER, ForeignKey(column="statuses.id", ondelete="RESTRICT"), nullable=False, index=True)

    user = relationship(argument="User", back_populates="orders")
    status = relationship(argument="Status", back_populates="orders")
    items = relationship(argument="OrderItem", back_populates="order")


class User(Base):
    __tablename__ = "users"

    name = Column(VARCHAR(24), nullable=False, unique=True)
    email = Column(VARCHAR(24), nullable=False, unique=True)
    orders = relationship(argument="Orders", back_populates="user")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id = Column(INTEGER, ForeignKey(column="orders.id", ondelete="RESTRICT"), nullable=False, index=True)
    product_id = Column(INTEGER, ForeignKey(column="products.id", ondelete="RESTRICT"), nullable=False, index=True)

    product = relationship(argument="Product")
    order = relationship(argument="Order", back_populates="items")


class Category(Base):
    __tablename__ = "categories"

    name = Column(VARCHAR(24), nullable=False, unique=True)
    products = relationship(argument="Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    category_id = Column(INTEGER, ForeignKey(column="categories.id", ondelete="RESTRICT"), nullable=False, index=True)

    category = relationship(argument=Category, back_populates="products")


engine = create_engine("sqlite:///db_homework.sqlite3")
Base.metadata.create_all(bind=engine)
