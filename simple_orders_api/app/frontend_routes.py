from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

frontend_router = APIRouter()


@frontend_router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@frontend_router.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@frontend_router.get("/register", response_class=HTMLResponse)
async def read_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@frontend_router.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@frontend_router.get("/customers/add", response_class=HTMLResponse)
async def add_customer_form(request: Request):
    return templates.TemplateResponse("customer.html", {"request": request})


@frontend_router.get("/customers/view", response_class=HTMLResponse)
async def view_customers(request: Request):
    return templates.TemplateResponse("view-customers.html", {"request": request})


@frontend_router.get("/customers/update/{customer_id}", response_class=HTMLResponse)
async def update_customer_form(customer_id: int, request: Request):
    return templates.TemplateResponse(
        "update-customer.html", {"request": request, "customer_id": customer_id}
    )


@frontend_router.get("/products/add", response_class=HTMLResponse)
async def add_product_form(request: Request):
    return templates.TemplateResponse("product.html", {"request": request})


@frontend_router.get("/products/view", response_class=HTMLResponse)
async def view_products(request: Request):
    return templates.TemplateResponse("view-products.html", {"request": request})


@frontend_router.get("/products/update/{product_id}", response_class=HTMLResponse)
async def update_product_form(product_id: int, request: Request):
    return templates.TemplateResponse(
        "update-product.html", {"request": request, "product_id": product_id}
    )


@frontend_router.get("/orders/add", response_class=HTMLResponse)
async def add_order_form(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})


@frontend_router.get("/orders/view", response_class=HTMLResponse)
async def view_orders(request: Request):
    return templates.TemplateResponse("view-orders.html", {"request": request})


@frontend_router.get("/orders/update/{order_id}", response_class=HTMLResponse)
async def update_order_form(order_id: int, request: Request):
    return templates.TemplateResponse(
        "update-order.html", {"request": request, "order_id": order_id}
    )
