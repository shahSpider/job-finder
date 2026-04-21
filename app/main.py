from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import engine
from app.db.base import Base
from app.models.user import User
from app.models.job import Job
from app.models.source import JobSource
from app.api.users import router as users_router
from app.api.jobs import router as jobs_router
from app.api.sources import router as sources_router
from app.workers.scheduler import start_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = start_scheduler()

    # Startup logic
    yield

    scheduler.shutdown()
    # Shutdown logic (optional)
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(sources_router)


@app.get("/")
async def root():
    return {"message": "Hello I'm Job Finder API!"}