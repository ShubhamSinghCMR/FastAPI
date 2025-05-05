from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(
    tags=["Products"],
    responses={404: {"description": "Not found"}, 400: {"description": "Bad request"}},
)


@router.post(
    "/",
    response_model=schemas.ProductOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new product",
    response_description="Product created successfully",
)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Add a new **product** with name and price.

    - Expects a name (string) and price (float)
    - Returns the newly created product object
    """
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get(
    "/{product_id}",
    response_model=schemas.ProductOut,
    summary="Get product by ID",
    response_description="Returns the product with the specified ID",
)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Fetch a **product** by its unique ID.

    Returns a 404 if not found.
    """
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put(
    "/{product_id}",
    response_model=schemas.ProductOut,
    summary="Update a product",
    response_description="Returns the updated product",
)
def update_product(
    product_id: int, updates: schemas.ProductUpdate, db: Session = Depends(get_db)
):
    """
    Modify an existing product's **name or price**.

    Partial updates are allowed — only fields provided will be changed.
    """
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for field, value in updates.dict(exclude_unset=True).items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a product",
    response_description="Product deleted successfully",
)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Permanently delete a product by **ID**.

    Returns 204 status code with no response body.
    """
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return None
