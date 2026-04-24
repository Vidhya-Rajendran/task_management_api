import asyncio
from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, Base
from app.routers.task_router import router as task_router

app = FastAPI(title="Task CRUD App with FastAPI + PostgreSQL + Docker")


async def wait_for_db(max_retries: int = 20, delay: int = 3):
    for attempt in range(1, max_retries + 1):
        try:
            async with engine.begin() as conn:
                await conn.execute(text("SELECT 1"))
                await conn.run_sync(Base.metadata.create_all)
            print("Database is ready.")
            return
        except Exception as e:
            print(f"Database not ready yet (attempt {attempt}/{max_retries}): {e}")
            await asyncio.sleep(delay)

    raise RuntimeError("Could not connect to the database after multiple retries.")


@app.on_event("startup")
async def startup():
    await wait_for_db()


app.include_router(task_router)


@app.get("/")
async def root():
    return {"message": "Task API is running with PostgreSQL in Docker"}