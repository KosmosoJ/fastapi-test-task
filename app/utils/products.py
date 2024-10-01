from sqlalchemy.ext.asyncio import AsyncSession
from schema.products import ProductEdit
from sqlalchemy import select
from database.models import Product
from fastapi import HTTPException, status


async def get_all_products(session: AsyncSession):
    """ Получение всех продуктов из БД """
    products = await session.execute(select(Product))
    products = products.scalars().all()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return products


async def get_product_by_id(product_id: int, session: AsyncSession):
    """ Поиск продукта по ID """
    product = await session.execute(select(Product).where(Product.id == product_id))
    product = product.scalars().first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product


async def create_product(product_info: ProductEdit, session: AsyncSession):
    """ Добавление продукта в базу данных  """
    product = Product(
        name=product_info.name,
        description=product_info.description,
        price=product_info.price,
        quantity=product_info.quantity,
    )

    session.add(product)
    await session.commit()
    return product


async def edit_product(
    product_id: int, product_info: ProductEdit, session: AsyncSession
):
    """ Изменение продукта в базе данных """
    product = await session.execute(select(Product).where(Product.id == product_id))
    product = product.scalars().first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID `{product_id}` not found ",
        )

    product.name, product.description, product.price, product.quantity = (
        product_info.name,
        product_info.description,
        product_info.price,
        product_info.quantity,
    )
    await session.commit()
    return product
