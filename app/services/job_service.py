from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate, JobResponse
import uuid
from app.core.redis import redis_client
import json
from fastapi.encoders import jsonable_encoder
from app.core.logger import logger

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


async def get_jobs_service(page: int, page_size: int, offset: int, db: AsyncSession):
    
    try:
        logger.info(f"Fetching jobs page={page}, size={page_size}")
        cache_key = f"jobs:{page}:{page_size}"
        # Check cache
        cached = await redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
        
        # If not cached → query DB
        result = await db.execute(select(Job).offset(offset).limit(page_size))

        jobs = result.scalars().all()

        jobs_data = [
            JobResponse.model_validate(job).model_dump()
            for job in jobs
        ]
        response = {
            "items": jobs_data,
            "total": len(jobs_data),
            "page": page,
            "page_size": page_size
        }

        json_ready = jsonable_encoder(response)
        # Store in Redis (TTL = 60 seconds)
        await redis_client.set(cache_key, json.dumps(json_ready), exx=60)

        return response
    except Exception as e:
        logger.error(f"Error fetching jobs: {e}")
        return {"error": "Failed to fetch jobs"}

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