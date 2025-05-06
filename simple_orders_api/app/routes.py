from fastapi import APIRouter, Depends

from app.api import auth, customer, order, product
from app.dependencies.auth import get_current_user

api_v1 = APIRouter()

# Public endpoints (no auth)
api_v1.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Protected endpoints
api_v1.include_router(
    customer.router,
    prefix="/customers",
    tags=["Customers"],
    dependencies=[Depends(get_current_user)],
)

api_v1.include_router(
    product.router,
    prefix="/products",
    tags=["Products"],
    dependencies=[Depends(get_current_user)],
)

api_v1.include_router(
    order.router,
    prefix="/orders",
    tags=["Orders"],
    dependencies=[Depends(get_current_user)],
)

# Export the versioned API group
router = APIRouter()
router.include_router(api_v1, prefix="/api/v1")  # 👈 group everything under /api/v1
