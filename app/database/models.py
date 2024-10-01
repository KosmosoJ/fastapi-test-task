from .database import Base
from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, ForeignKey
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'
    
    
    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    price = Column(Float(), nullable=False)
    quantity = Column(Integer(), default=0)
    
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    order_id = Column(String(), nullable=False)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.now())
    status = Column(String(), nullable=False, default='В процессе')
    
    
class OrderItem(Base):
    __tablename__ = 'orderitems'
    
    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    product_id= Column(ForeignKey('products.id'), nullable=False)
    product_quantity = Column(Integer(), nullable=False, default=1)