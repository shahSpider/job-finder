from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.source import JobSource
from app.schemas.source import JobSourceCreate, JobSourceResponse, JobSourceUpdate

async def create_source(db: AsyncSession, data: JobSourceCreate):
    source = JobSource(**data.dict())
    db.add(source)
    await db.commit()
    await db.refresh(source)
    return source


async def get_sources(db: AsyncSession):
    result = await db.execute(select(JobSource))
    return result.scalars().all()

async def update_source(db: AsyncSession, source_id: str, source_data: JobSourceUpdate):
    result = await db.execute(select(JobSource).where(JobSource.id == source_id))
    source = result.scalar_one_or_none()
    if source:
        data = source_data.dict(exclude_unset=True)
        for key, value in data.items():
            setattr(source, key, value)
        await db.commit()
        await db.refresh(source)
        return source
    return False

async def delete_source(db: AsyncSession, source_id: str):
    result = await db.execute(select(JobSource).where(JobSource.id == source_id))
    source = result.scalar_one_or_none()
    if source:
        await db.delete(source)
        await db.commit()
        return {"message": f"Source with ID {source_id} deleted successfully"}
    return False