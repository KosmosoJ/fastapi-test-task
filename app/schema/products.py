from pydantic import BaseModel
from typing import Optional

class ProductEdit(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    quantity:int
    

    
    