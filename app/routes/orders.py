from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.orders as orders_utils


router = APIRouter()


@router.get('/orders')
async def get_all_orders(session:AsyncSession = Depends(get_session)):
    orders = await orders_utils.get_all_orders(session)
    return orders
    
@router.get('/orders/{order_id}')
async def get_order_id(order_id:int, session:AsyncSession = Depends(get_session)):
    order = await orders_utils.get_order_id(order_id, session)
    return order
    
@router.post('/orders')
async def create_order(order_info, session:AsyncSession = Depends(get_session)):
    ...
    
@router.patch('/orders/{order_id}/status')
async def update_order_status(order_id:int, session:AsyncSession = Depends(get_session)):
    order = await orders_utils.edit_order_status(order_id, session)
    return order 
    
