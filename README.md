FastAPI Fundamentals and Database Setup

Objective: Set up the development environment, understand API routing, build a database-driven CRUD application, and establish the PostgreSQL foundation.

Concepts Mastered

Environment Setup: Configured Python virtual environments and VS Code for backend development.

FastAPI Basics: Built initial path operations, handled HTTP requests (GET, POST, PUT, DELETE), and managed response status codes (e.g., 201 Created, 204 No Content, 404 Not Found).

Data Validation: Implemented strict schema validation using Pydantic models.

API Testing: Utilized Postman to test endpoints and save request collections.

Database Foundation: Installed and configured PostgreSQL and pgAdmin 4.

Raw SQL Queries: Executed basic SQL commands including INSERT, SELECT, and filtering data using WHERE, IN, LIKE, ORDER BY, and LIMIT/OFFSET.

Tech Stack and Tools Used

Framework: FastAPI

Language: Python 3

Validation: Pydantic

API Client: Postman

Database Engine: PostgreSQL

Database GUI: pgAdmin 4

How to Run

Ensure PostgreSQL is running on Port 5432.

Install dependencies: pip install fastapi uvicorn psycopg2-binary.

Start the server: uvicorn main:app --reload.
