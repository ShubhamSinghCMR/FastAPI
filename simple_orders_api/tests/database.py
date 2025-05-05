from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base

TEST_DATABASE_URL = "postgresql://postgres:password@localhost:5432/orders_test"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
