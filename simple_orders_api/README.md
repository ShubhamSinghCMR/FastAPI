# Project Setup in Windows:
1. Create virtual environment
`python -m venv venv`

2. Activate virtual environment:
`venv/Scripts/activate`

3. Install project requirents:
`pip install -r requirements.txt`

4. Setup database (Make sure psql is running):
- alembic revision -m "Initial tables"

# After Code Changes:
1. Run linters & formatters:
isort .; black .; ruff check . --fix; ruff check . --select F401 --fix

2. Run Test:
pytest -v

# Project Execution:
1. Run the project:
`uvicorn app.main:app --reload` 
