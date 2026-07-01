from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.task import Task   # <-- HERE (top)
from app.models.schemas import TaskCreate, TaskResponse
from app.services.task_service import( create_task_service, get_tasks_service,update_task_service,delete_task_service,complete_task_service)
from app.utils.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: 
    Session = Depends(get_db),current_user: User = Depends(get_current_user)
):
    return create_task_service(db, task, current_user)

@router.get("/tasks",response_model=list[TaskResponse])
def get_tasks(completed: bool|None = None, search: str|None = None, sort_order: str = "asc",skip: int = 0,limit:int = 10,db:Session =Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_tasks_service(db=db,completed = completed,search = search,sort_order=sort_order,skip=skip,limit=limit,  user=current_user)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = delete_task_service(db, task_id, current_user)
    
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    
   
    
    return {"message": "Task deleted"}

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_task = update_task_service(db,task_id,task,current_user)

    if not updated_task:
        raise HTTPException(status_code=404,detail="Task not found")

   
    return updated_task

@router.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = complete_task_service(db, task_id,current_user)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task    