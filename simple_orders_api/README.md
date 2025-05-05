# First Time:

pip install -r requirements.txt

alembic init alembic


Create initial Migration: - Open Postgresql before it if not using docker
alembic revision --autogenerate -m "Initial tables"
alembic upgrade head

# Run:
Run linters & formatters
isort .; black .; ruff check . --fix; ruff check . --select F401 --fix

Run Test:
pytest -v

Execute:
uvicorn app.main:app --reload  
