from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from database.models import Order, OrderItem
from sqlalchemy import select 


async def get_all_orders(session:AsyncSession):
    orders = await session.execute(select(Order))
    orders = orders.scalars().all()
    
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return orders

async def get_order_id(order_id:int, session:AsyncSession):
    order = await session.execute(select(Order).where(Order.id == order_id))
    order = order.scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
    return order 

async def create_order(order_products:list, session:AsyncSession):
    ...

async def edit_order_status(order_id:int, session:AsyncSession):
    order = (await session.execute(select(Order).where(Order.id == order_id))).scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
    return order 