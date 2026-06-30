Day 1: FastAPI Fundamentals and Database Setup

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


Day 2:

FastAPI and PostgreSQL CRUD Backend

A robust RESTful API built with FastAPI and PostgreSQL. This project implements a complete backend system with database integration using SQLAlchemy (ORM) and strict data validation using Pydantic.

Tech Stack and Tools Used (So Far)

Framework: FastAPI
Language: Python 3
Validation: Pydantic
API Client: Postman
Database Engine: PostgreSQL
Database GUI: pgAdmin 4

Project Structure

The code is modularized into separate files for better maintainability:

main.py: Contains the FastAPI application instance and all routing logic.
database.py: Handles the PostgreSQL database connection and session management.
models.py: Defines the SQLAlchemy ORM models (Database Tables).
schemas.py: Defines Pydantic models for request body validation and response serialization.

Setup Instructions

Prerequisites
Make sure you have Python 3 installed on your machine and PostgreSQL running locally.

Environment Setup
Create a virtual environment and install the required dependencies:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install fastapi[all] psycopg2 sqlalchemy

Database Configuration
Open database.py and update the SQLALCHEMY_DATABASE_URL with your local PostgreSQL credentials:
SQLALCHEMY_DATABASE_URL = "postgresql://:@localhost/<database_name>"

Run the Server
Start the Uvicorn ASGI server:
uvicorn main:app --reload

API Endpoints

Method | Endpoint | Description
GET | /posts | Retrieve all posts from the database.
POST | /posts | Create a new post.
GET | /posts/{id} | Retrieve a specific post by its ID.
PUT | /posts/{id} | Update an existing post.
DELETE | /posts/{id} | Delete a post.

Interactive API Documentation

Once the server is running, you can test all endpoints directly from your browser via the built-in Swagger UI:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
