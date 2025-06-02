from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.secure import get_current_user
from app.crud.task import get_tasks, create_task, update_task, delete_task
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task, current_user.id)

@router.get("/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tasks(db, skip, limit)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_tasks(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    db_task = get_tasks(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(db, db_task, task_update)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_tasks(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, db_task)
    return {"message": "Task deleted successfully"}
