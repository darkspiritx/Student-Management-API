# Student Management API

A RESTful Student Management API built using Python, FastAPI, PostgreSQL, and SQLAlchemy.

## Features

- Create, Read, Update and Delete students (CRUD)
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request and response validation
- Pagination with total count and total pages
- Search students by course
- HTTP error handling
- Automated API testing using Pytest

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- HTTPX

## Project Structure

```text
Student-Management-API/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   └── students.py
├── test_main.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Student-Management-API
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg pytest httpx
```

Configure your PostgreSQL database connection in `database.py`.

Run the application:

```bash
python -m uvicorn main:app --reload
```

## API Documentation

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
python -m pytest -v
```

## Author

Mohit Prajapati

GitHub: https://github.com/darkspiritx