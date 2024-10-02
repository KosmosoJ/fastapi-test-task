from pydantic import BaseModel, Json
from typing_extensions import TypedDict
from datetime import datetime



class OrderBase(BaseModel):
    id: int
    order_id:str
    created_at:datetime
    status:str


class OrderItem(BaseModel):
    id:int
    order_id:str
    product_id:int
    product_quantity:int

class OrderDetailed(OrderBase):
    ordersitems:list[OrderItem]

class Products_info(TypedDict):
    product_id:int
    quantity:int

class OrderItems(TypedDict):
    products:list[Products_info]
    
    