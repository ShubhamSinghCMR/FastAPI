from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr


class CustomerUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class CustomerOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {"from_attributes": True}
