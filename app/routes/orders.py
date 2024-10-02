from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.orders as orders_utils
import schema.orders as orders_schema


router = APIRouter()

async def return_order_detailed(order):
    """ Возвращение подробной информации о заказе """
    return orders_schema.OrderDetailed(
        id=order.id,
        order_id=order.order_id,
        ordersitems=[
            orders_schema.OrderItem(
                id=orderitem.id,
                order_id=orderitem.order_id,
                product_id=orderitem.product_id,
                product_quantity=orderitem.product_quantity,
            )
            for orderitem in order.ordersitems
        ],
        created_at=order.created_at,
        status=order.status,
    )

@router.get("/orders", response_model=list[orders_schema.OrderBase])
async def get_all_orders(session: AsyncSession = Depends(get_session)):
    """Вывод всех заказов"""
    orders = await orders_utils.get_all_orders(session)
    return orders


@router.get("/orders/{order_id}", response_model=orders_schema.OrderDetailed)
async def get_order_id(order_id: str, session: AsyncSession = Depends(get_session)):
    """Вывод заказа по order.order_id"""
    order = await orders_utils.get_order_id(order_id, session)
    return await return_order_detailed(order)


@router.post("/orders")
async def create_order(
    order_info: orders_schema.OrderItems, session: AsyncSession = Depends(get_session)
):
    """Создание заказа"""
    order = await orders_utils.create_order(order_info, session)
    return order


@router.patch("/orders/{order_id}/status")
async def update_order_status(
    order_id: str, session: AsyncSession = Depends(get_session)
):
    """Обновление статуса заказа"""
    order = await orders_utils.edit_order_status(order_id, session)
    return await return_order_detailed(order)
