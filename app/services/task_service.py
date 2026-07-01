from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.schemas import TaskCreate
from app.utils.logger import logger
from app.models.user import User


def create_task_service(db: Session, task: TaskCreate, user: User):
    new_task = Task(title=task.title,completed = task.completed,user_id=user.id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    logger.info(f"Task created: {task.title}")

    return new_task


def get_tasks_service(db: Session,  user: User,completed: bool = None,search: str = None,sort_order: str = "asc",skip: int = 0,limit: int =10):
    query = db.query(Task).filter(Task.user_id == user.id)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))
    if sort_order == "desc":
        query = query.order_by(Task.created_at.desc())
    else:
        query = query.order_by(Task.created_at.asc())

    return query.offset(skip).limit(limit).all()

def delete_task_service(db: Session, task_id: int, user: User):
    task = db.query(Task).filter(Task.id == task_id,Task.user_id == user.id).first()

    if not task:
        return None

    logger.info(f"Task deleted: {task.title}")
    db.delete(task)
    db.commit()

    return task


def update_task_service(db: Session, task_id: int, task_data: TaskCreate,user: User):
    existing_task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not existing_task:
        return None

    existing_task.title = task_data.title
    existing_task.completed = task_data.completed

    logger.info(f"task updated: {existing_task.title}")
    db.commit()
    db.refresh(existing_task)

    return existing_task

def complete_task_service(db: Session, task_id: int,user: User):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not task:
        return None

    task.completed = True

    logger.info(f"Task completed: {task.title}")
    db.commit()
    db.refresh(task)

    return task