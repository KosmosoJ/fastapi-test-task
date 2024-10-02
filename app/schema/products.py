from pydantic import BaseModel
from typing import Optional

    
    
class ProductBase(BaseModel):
    name:str
    description:str
    price:float
    quantity:int

class ProductEdit(ProductBase):
    description:Optional[str] = None

    
    