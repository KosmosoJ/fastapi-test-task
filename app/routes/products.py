from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get('/products')
async def get_all_products(session:AsyncSession = Depends(get_session)):
    ...
    
@router.get('/products/{product_id}')
async def get_product_id(product_id:int, session:AsyncSession = Depends(get_session)):
    ...
    
@router.post('/products')
async def create_product(product_info, session:AsyncSession = Depends(get_session)):
    ...
    
@router.put('/products/{product_id}')
async def update_product(product_id:int, product_info, session:AsyncSession = Depends(get_session)):
    ...
    
@router.delete('/products/{product_id}')
async def delete_product(product_id:int, session:AsyncSession = Depends(get_session)):
    ...
    
    