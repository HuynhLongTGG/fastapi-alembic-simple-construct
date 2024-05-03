## Project Overview

This project is a simple yet powerful API built using FastAPI, Alembic, and includes authentication. It provides a solid foundation for developers to start building their applications with ease.

### Features:

- **FastAPI**: Utilizes FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

- **Alembic**: Integrates Alembic for database migrations. Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

- **Authentication**: Implements authentication for secure access to the API. This ensures that only authorized users can interact with the system.

- **Basic Database Structure**: Includes two fundamental tables: `User` and `Role`. This establishes a basic user management system with role-based access control.

## Getting Started

### Setting up PostgreSQL:
You can either set up PostgreSQL directly on your computer or use docker-compose from the source code.

### Installing dependencies:
Install the required libraries from the `requirements.txt` file using the command:
```bash
pip install -r requirements.txt
```

### Database Migration:
Use the following commands for database migration:
```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
# If errors occur, you can either drop tables or stop docker compose, delete files in the `versions` directory, and rerun the above commands
```

### Running the API:
Navigate to the `App` directory and run:
```bash
uvicorn main:app
```
