# Task Manager API

A RESTful Task Manager API built with FastAPI that allows users to securely manage their tasks.

## Features

- User Registration
- User Login with JWT Authentication
- Create Tasks
- View Tasks
- Update Tasks
- Delete Tasks
- Filter Tasks by Completion Status
- SQLite Database
- Password Hashing
- Input Validation
- Logging
- Unit Tests using Pytest

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- JWT
- Passlib
- Pytest

## Project Structure

```
app/
    database/
    models/
    routes/
    services/
    utils/
tests/
```

## Run the Project

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to access Swagger UI.

## Testing

```bash
pytest
```