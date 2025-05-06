from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(
    tags=["Orders"],
    responses={404: {"description": "Not found"}, 400: {"description": "Bad request"}},
)


@router.get("/", response_model=List[schemas.order.OrderOut])
def list_orders(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Order).all()


@router.post(
    "/",
    response_model=schemas.OrderOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new order",
    response_description="Order successfully created",
)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    """
    Place a new order for a **specific customer** with one or more product IDs.

    - Validates if customer and all product IDs exist.
    - Calculates total cost and creates order-product links.
    """
    customer = (
        db.query(models.Customer)
        .filter(models.Customer.id == order.customer_id)
        .first()
    )
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    products = (
        db.query(models.Product).filter(models.Product.id.in_(order.product_ids)).all()
    )
    if len(products) != len(order.product_ids):
        raise HTTPException(status_code=404, detail="One or more products not found")

    total = sum([p.price for p in products])
    new_order = models.Order(customer_id=order.customer_id, total_cost=total)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for product in products:
        link = models.OrderProduct(order_id=new_order.id, product_id=product.id)
        db.add(link)
    db.commit()
    db.refresh(new_order)

    return new_order


@router.get(
    "/{order_id}",
    response_model=schemas.OrderOut,
    summary="Retrieve a specific order",
    response_description="Returns the order with all product links",
)
def get_order(order_id: int, db: Session = Depends(get_db)):
    """
    Fetch details of an order by its **ID**.
    """
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put(
    "/{order_id}",
    response_model=schemas.OrderOut,
    summary="Update an order's products",
    response_description="Updated order with new products",
)
def update_order(
    order_id: int, updates: schemas.OrderUpdate, db: Session = Depends(get_db)
):
    """
    Update the list of **products** in an order.

    - Removes old links
    - Recalculates total cost
    - Links new products
    """
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    products = (
        db.query(models.Product)
        .filter(models.Product.id.in_(updates.product_ids))
        .all()
    )
    if len(products) != len(updates.product_ids):
        raise HTTPException(status_code=404, detail="One or more products not found")

    db.query(models.OrderProduct).filter(
        models.OrderProduct.order_id == order_id
    ).delete()

    for product in products:
        link = models.OrderProduct(order_id=order.id, product_id=product.id)
        db.add(link)

    order.total_cost = sum(p.price for p in products)
    db.commit()
    db.refresh(order)
    return order


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an order",
    response_description="Order deleted successfully",
)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    """
    Delete an order by **ID**.

    - Also removes all associated product links.
    """
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.query(models.OrderProduct).filter(
        models.OrderProduct.order_id == order_id
    ).delete()
    db.delete(order)
    db.commit()
    return None
