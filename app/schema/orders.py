from pydantic import BaseModel



class OrderBase(BaseModel):
    id: int
    order_id:str
    created_at:str
    status:str


    
    