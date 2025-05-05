from datetime import datetime
from typing import List

from pydantic import BaseModel

from .product import ProductOut


class OrderCreate(BaseModel):
    customer_id: int
    product_ids: List[int]


class OrderOut(BaseModel):
    id: int
    customer_id: int
    total_cost: float
    created_at: datetime
    products: List[ProductOut]

    model_config = {"from_attributes": True}


class OrderUpdate(BaseModel):
    product_ids: List[int]


class OrderOutForCustomer(BaseModel):
    id: int
    total_cost: float
    created_at: datetime
    products: List[ProductOut]

    model_config = {"from_attributes": True}
