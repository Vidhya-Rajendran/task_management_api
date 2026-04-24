from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate


class TaskService:
    @staticmethod
    async def create_task(db: AsyncSession, task_data: TaskCreate) -> Task:
        new_task = Task(
            title=task_data.title,
            description=task_data.description,
        )
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)
        return new_task

    @staticmethod
    async def get_all_tasks(db: AsyncSession) -> list[Task]:
        result = await db.execute(select(Task))
        return result.scalars().all()

    @staticmethod
    async def get_task_by_id(db: AsyncSession, task_id: int) -> Task | None:
        result = await db.execute(select(Task).where(Task.id == task_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_task(db: AsyncSession, task: Task, task_data: TaskUpdate) -> Task:
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.is_completed is not None:
            task.is_completed = task_data.is_completed

        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def delete_task(db: AsyncSession, task: Task) -> None:
        await db.delete(task)
        await db.commit()