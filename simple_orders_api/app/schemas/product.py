from pydantic import BaseModel, condecimal


class ProductCreate(BaseModel):
    name: str
    price: condecimal(gt=0)


class ProductOut(BaseModel):
    id: int
    name: str
    price: float

    model_config = {"from_attributes": True}


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
