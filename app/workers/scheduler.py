from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import select

from app.core.database import AsyncSessionLocal as async_session_maker
from app.models.source import JobSource
from app.pipelines.job_pipeline import run_job_pipeline


scheduler = AsyncIOScheduler()


async def fetch_all_sources():
    async with async_session_maker() as db:
        result = await db.execute(select(JobSource).where(JobSource.is_active == True))
        sources = result.scalars().all()
        print(f"Scheduler: Found {len(sources)} active sources. Fetching jobs...")
        for source in sources:
            await run_job_pipeline(db, source)


def start_scheduler():
    print("Starting scheduler...")
    scheduler.add_job(fetch_all_sources, "interval", minutes=1000)
    scheduler.start()
    return scheduler