from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL, BOOLEAN, CheckConstraint, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Status(Base):
    __tablename__ = "statuses"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(10), nullable=False, unique=True)

    orders = relationship(argument="Order", back_populates="status")


class Order(Base):
    __tablename__ = "orders"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(INTEGER, ForeignKey(column="users", ondelete="RESTRICT"), nullable=False, index=True)
    status_id = Column(INTEGER, ForeignKey(column="statuses", ondelete="RESTRICT"), nullable=False, index=True)

    user = relationship(argument="User", back_populates="users")
    status = relationship(argument="Status", back_populates="statuses")


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(24), nullable=False, unique=True)
    email = Column(VARCHAR(24), nullable=False, unique=True)
    orders = relationship(argument="Orders", back_populates="user")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    order_id = Column(INTEGER, ForeignKey(column="orders", ondelete="RESTRICT"), nullable=False, index=True)
    product_id = Column(INTEGER, ForeignKey(column="products", ondelete="RESTRICT"), nullable=False, index=True)

    product = relationship(argument="Product", back_populates="products")
    order = relationship(argument="Order", back_populates="orders")


class Category(Base):
    __tablename__ = "categories"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(24), nullable=False, unique=True)
    product = relationship(argument="Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    category_id = Column(INTEGER, ForeignKey(column="categories", ondelete="RESTRICT"), nullable=False, index=True)

    category = relationship(argument=Category, back_populates="products")


engine = create_engine("sqlite:///db_homework.sqlite3")
Base.metadata.create_all(bind=engine)
