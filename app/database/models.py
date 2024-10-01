from .database import Base
from sqlalchemy import Column, String, Integer


class Model(Base):
    __tablename__ = 'models'
    
    
    id = Column(Integer(), primary_key=True, index=True)