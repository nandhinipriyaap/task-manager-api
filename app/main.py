from fastapi import FastAPI
from app.database.db import engine, Base
from app.routes import task_routes
from app.routes import auth_routes
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def home():
    return {"message": "Task Manager API is running"}