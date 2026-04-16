from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate, JobResponse
import uuid

async def create_job_service(db: AsyncSession, job_data: JobCreate):
    job = Job(
        title=job_data.title,
        description=job_data.description,
        company=job_data.company,
        location=job_data.location,
        salary=job_data.salary,
        url=job_data.url
    )
    db.add(job)
    await db.commit()
    await db.refresh(job)
    return job


async def get_jobs_service(db: AsyncSession):
    result = await db.execute(select(Job))
    return result.scalars().all()

async def get_job_by_id_service(db: AsyncSession, job_id: str):
    result = await db.execute(select(Job).where(Job.id == job_id))
    return result.scalar_one_or_none()

async def delete_job_service(db: AsyncSession, job_id: str):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if job:
        await db.delete(job)
        await db.commit()
        return {"message": f"Job with ID {job_id} deleted successfully"}
    return False

async def update_job_service(db: AsyncSession, job_id: str, job_data: JobUpdate):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if job:
        data = job_data.dict(exclude_unset=True)
        for key, value in data.items():
            setattr(job, key, value)
        await db.commit()
        await db.refresh(job)
        return job
    return False