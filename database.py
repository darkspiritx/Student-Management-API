from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in .env file")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

try:
    with engine.connect() as connection:
        print("Database Connected Successfully!.")
except Exception as e:
    print("Database Connection Failed!")
    print(e)