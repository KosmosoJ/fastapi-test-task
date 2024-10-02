from .database import Base
from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

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
    order_id = Column(String(), nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=False), default=datetime.now())
    status = Column(String(), nullable=False, default='В процессе')
    
    ordersitems = relationship('OrderItem', back_populates='order', lazy='joined')
    
    
class OrderItem(Base):
    __tablename__ = 'orderitems'
    
    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    order_id = Column(ForeignKey('orders.order_id', ondelete='SET NULL'), nullable=False)
    product_id= Column(ForeignKey('products.id', ondelete='SET NULL'), nullable=False)
    product_quantity = Column(Integer(), nullable=False, default=1)
    
    order = relationship('Order', back_populates='ordersitems')