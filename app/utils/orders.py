from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from database.models import Order, OrderItem