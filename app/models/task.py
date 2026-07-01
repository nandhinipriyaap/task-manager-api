from sqlalchemy import Column, Integer, String,DateTime,Boolean, ForeignKey
from app.database.db import Base
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean,default=False)
    user_id = Column(Integer, ForeignKey("users.id"))


    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
    DateTime(timezone=True),
    server_default=func.now(),
    onupdate=func.now()
    )