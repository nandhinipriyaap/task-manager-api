# Task Manager API

A RESTful Task Manager API built with **FastAPI** that enables users to securely manage their personal tasks using **JWT Authentication**. The project follows a clean architecture with separate routes, services, models, and utilities.

---

## Features

- User Registration
- User Login with JWT Authentication
- Password Hashing using bcrypt
- Create Task
- Get All Tasks
- Update Task
- Delete Task
- Mark Task as Completed
- User-specific Task Access
- Logging
- Automated Testing using Pytest

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- Pytest
- Git & GitHub

---

## Project Structure

```text
task-manager-api/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── tests/
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nandhinipriyaap/task-manager-api.git
```

Move into the project:

```bash
cd task-manager-api
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Once the server starts, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will be available.

---

## Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./tasks.db
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT token |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| PATCH | `/tasks/{task_id}/complete` | Mark a task as completed |
| DELETE | `/tasks/{task_id}` | Delete a task |





## Running Tests

```bash
pytest
```

---

## Future Improvements

- PostgreSQL support
- Docker
- Deployment
- Refresh Tokens
- CI/CD Pipeline

---

## Author

**Nandhinipriyaa Prabhakar**

GitHub: https://github.com/nandhinipriyaap