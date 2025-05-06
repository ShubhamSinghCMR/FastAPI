from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import router

app = FastAPI()

app.include_router(router)

# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="app/templates")


# Route for the home page
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Route for the login page
@app.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Route for the register page
@app.get("/register", response_class=HTMLResponse)
async def read_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# Route for the dashboard page
@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


# Route for Add Customer page
@app.get("/customers/add", response_class=HTMLResponse)
async def add_customer_form(request: Request):
    return templates.TemplateResponse("customer.html", {"request": request})


# Route for View Customers page
@app.get("/customers/view", response_class=HTMLResponse)
async def view_customers(request: Request):
    return templates.TemplateResponse("view-customers.html", {"request": request})


# Route for Update Customer page
@app.get("/customers/update/{customer_id}", response_class=HTMLResponse)
async def update_customer_form(customer_id: int, request: Request):
    return templates.TemplateResponse(
        "update-customer.html", {"request": request, "customer_id": customer_id}
    )


# Route for Add Product page
@app.get("/products/add", response_class=HTMLResponse)
async def add_product_form(request: Request):
    return templates.TemplateResponse("product.html", {"request": request})


# Route for View Products page
@app.get("/products/view", response_class=HTMLResponse)
async def view_products(request: Request):
    return templates.TemplateResponse("view-products.html", {"request": request})


# Route for Update Product page
@app.get("/products/update/{product_id}", response_class=HTMLResponse)
async def update_product_form(product_id: int, request: Request):
    return templates.TemplateResponse(
        "update-product.html", {"request": request, "product_id": product_id}
    )


# Route for Create Order page
@app.get("/orders/add", response_class=HTMLResponse)
async def add_order_form(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})


# Route for View Orders page
@app.get("/orders/view", response_class=HTMLResponse)
async def view_orders(request: Request):
    return templates.TemplateResponse("view-orders.html", {"request": request})


# Route for Update Order page
@app.get("/orders/update/{order_id}", response_class=HTMLResponse)
async def update_order_form(order_id: int, request: Request):
    return templates.TemplateResponse(
        "update-order.html", {"request": request, "order_id": order_id}
    )
