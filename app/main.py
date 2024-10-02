from fastapi import FastAPI
from routes.products import router as products_router
from routes.orders import router as orders_router

app = FastAPI()

app.include_router(products_router, tags=['products'])
app.include_router(orders_router, tags=['orders'])