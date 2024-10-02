from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import utils.products as products_utils
import schema.products as products_schema

router = APIRouter()

@router.get('/products', response_model=list[products_schema.ProductBase])
async def get_all_products(session:AsyncSession = Depends(get_session)):
    """ Вывод всех найденных продуктов """
    products = await products_utils.get_all_products(session)
    return products
    
@router.get('/products/{product_id}', response_model=products_schema.ProductBase)
async def get_product_id(product_id:int, session:AsyncSession = Depends(get_session)):
    """ Вывод найденного продукта по ID """
    product = await products_utils.get_product_by_id(product_id, session)
    return product
    
@router.post('/products', response_model=products_schema.ProductBase)
async def create_product(product_info:products_schema.ProductEdit, session:AsyncSession = Depends(get_session)):
    """ Создание нового продукта с выводом пользователю """
    product = await products_utils.create_product(product_info, session)
    return product
    
@router.put('/products/{product_id}', response_model=products_schema.ProductBase)
async def update_product(product_id:int, product_info:products_schema.ProductEdit, session:AsyncSession = Depends(get_session)):
    """ Обновление продукта """
    product = await products_utils.edit_product(product_id, product_info, session)
    return product
    
@router.delete('/products/{product_id}', response_model=products_schema.ProductBase)
async def delete_product(product_id:int, session:AsyncSession = Depends(get_session)):
    """ Удаление продукта """
    product = await products_utils.delete_product(product_id, session)
    return product    
    