from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from database.models import Order, OrderItem
from sqlalchemy import select 
import schema.orders as orders_schema
import random, string
import utils.products as products_utils


async def generate_random_string_for_orderid():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

async def get_all_orders(session:AsyncSession):
    """ Получение всех заказов из бд """
    orders = await session.execute(select(Order))
    orders = orders.unique().scalars().all()
    
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return orders

async def get_order_id(order_id:str, session:AsyncSession):
    """ Получение заказа по ID """
    order = await session.execute(select(Order).where(Order.order_id == order_id))
    
    order = order.scalars().first()
    
    
    
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
    return order 

async def create_order(order_products:orders_schema.OrderItems, session:AsyncSession):
    """ Создание заказа в бд """
    order = Order(order_id=await generate_random_string_for_orderid())
    session.add(order)
    for order_product in order_products['products']:
        product = await products_utils.get_product_by_id(order_product['product_id'], session)
        
        # Проверка наличия товара в бд 
        if product.quantity < order_product['quantity']:
            await session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Product with ID `{order_product["product_id"]}` not enough')
        
        order_item = OrderItem(order_id=order.order_id, product_id=product.id, product_quantity=order_product['quantity'])
        product.quantity -= order_product['quantity']
        session.add(order_item)

    
    await session.commit()
    return order 
    

async def edit_order_status(order_id:int, session:AsyncSession):
    order = (await session.execute(select(Order).where(Order.id == order_id))).scalars().first()
    
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if order.status == 'В процессе':
        order.status = 'Отправлен'
        await session.commit()
    elif order.status == 'Отправлен':
        order.status = 'Доставлен'
        await session.commit()

        
    return order 