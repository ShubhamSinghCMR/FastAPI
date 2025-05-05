from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(
    tags=["Customers"],
    responses={404: {"description": "Not found"}, 400: {"description": "Bad request"}},
)


@router.post(
    "/",
    response_model=schemas.CustomerOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer",
    response_description="Customer created successfully",
)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    """
    Register a new customer with **unique email**.

    - **name**: Full name of the customer
    - **email**: Must not be already registered
    """
    existing = (
        db.query(models.Customer)
        .filter(models.Customer.email == customer.email)
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_customer = models.Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


@router.get(
    "/{customer_id}",
    response_model=schemas.CustomerOut,
    summary="Get customer details",
    response_description="Returns a single customer",
)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a customer by **ID**.
    """
    customer = (
        db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    )
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.put(
    "/{customer_id}",
    response_model=schemas.CustomerOut,
    summary="Update customer info",
    response_description="Updated customer data",
)
def update_customer(
    customer_id: int, updates: schemas.CustomerUpdate, db: Session = Depends(get_db)
):
    """
    Update customer fields like **name** or **email**.

    Only provided fields will be updated.
    """
    customer = (
        db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    )
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    for field, value in updates.dict(exclude_unset=True).items():
        setattr(customer, field, value)

    db.commit()
    db.refresh(customer)
    return customer


@router.delete(
    "/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a customer",
    response_description="Customer deleted successfully",
)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """
    Delete a customer by **ID**.
    """
    customer = (
        db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    )
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    db.delete(customer)
    db.commit()
    return None


@router.get(
    "/{customer_id}/orders",
    response_model=List[schemas.order.OrderOutForCustomer],
    summary="Get all orders of a customer",
    response_description="List of orders placed by the customer",
)
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all orders made by a **specific customer**.
    """
    customer = (
        db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    )
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    orders = (
        db.query(models.Order).filter(models.Order.customer_id == customer_id).all()
    )
    return orders
