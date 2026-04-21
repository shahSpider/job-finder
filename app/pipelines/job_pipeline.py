from sqlalchemy import select
from app.models.job import Job
from app.fetchers.factory import get_fetcher
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.source import JobSourceCreate, JobSourceResponse

async def run_job_pipeline(db: AsyncSession, source: JobSourceResponse):
    fetcher = get_fetcher(source)

    raw_data = await fetcher.fetch()
    jobs_data = fetcher.parse(raw_data)

    print(f"Fetched {jobs_data} jobs from {source.name}")

    created_jobs = []

    for job_data in jobs_data:

        # 🔒 Deduplication
        result = await db.execute(
            select(Job).where(
                Job.title == job_data["title"],
                Job.company == job_data["company"],
                Job.source_id == source.id
            )
        )
        existing = result.scalar_one_or_none()

        if existing:
            continue

        job = Job(
            title=job_data["title"],
            description=job_data["description"],
            company=job_data["company"],
            location=job_data["location"],
            salary=job_data.get("salary"),
            url=job_data["url"],
            source_id=source.id
        )

        db.add(job)
        created_jobs.append(job)

    await db.commit()

    return created_jobs