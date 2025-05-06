# Simple Orders API

A full-stack web application for managing customers, products, and orders, built using **FastAPI**, **PostgreSQL**, and **Bootstrap**. It features a secure JWT-authenticated backend, an HTML/JS frontend, analytics dashboard, and complete CRUD functionality via a RESTful API.


## Features

### API Functionalities
- Create, update, delete customers, products, and orders
- Fetch detailed orders with product and customer info
- Auto-calculated order totals
- Email and ID validations
- Error handling with proper status codes

### Authentication
- JWT-based login, registration, and logout
- Token blacklist for secure logout
- Auth-protected API endpoints

### Frontend
- Minimal HTML + Bootstrap UI
- Dynamic forms for customer/product/order management
- Interactive order form with product quantity controls
- Analytics dashboard with:
  - Line chart of total sales over time
  - Table of top-selling products



## Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | FastAPI, SQLAlchemy     |
| Database   | PostgreSQL              |
| Migrations | Alembic                 |
| Frontend   | Jinja2, Bootstrap 5, JS |
| Auth       | JWT, OAuth2PasswordFlow |
| Testing    | pytest                  |
| DevOps     | Docker, .env config     |



## Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/ShubhamSinghCMR/FastAPI.git
cd simple_orders_api
```

2. Setup & activate virtual environment
 ```bash
 python -m venv venv
 venv/Scripts/activate
 pip install -r requirements.txt
```

3. Run Alembic Migrations
```bash
alembic upgrade head
```

## Run the App Locally
```bash
uvicorn app.main:app --reload
```

## After Code Update:
1. Run linters & formatters:
```bash
isort .; black .; ruff check . --fix; ruff check . --select F401 --fix
```

2. Run Test:
```bash
pytest -v
```
