from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.db.session import get_db
from app.schemas.source import JobSourceCreate, JobSourceResponse, JobSourceUpdate
from app.services.source_service import create_source, get_sources, update_source, delete_source


router = APIRouter(prefix="/sources", tags=["sources"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_job_source(source: JobSourceCreate, db: AsyncSession = Depends(get_db)):
    return await create_source(db=db, data=source)


@router.get("/", response_model=list[JobSourceResponse], status_code=status.HTTP_200_OK)
async def get_job_sources(db: AsyncSession = Depends(get_db)):
    return await get_sources(db=db)


@router.put("/{source_id}", response_model=JobSourceUpdate, status_code=status.HTTP_200_OK)
async def update_job_source(source_id: str, source_data: JobSourceUpdate, db: AsyncSession = Depends(get_db)):
    if not await update_source(db=db, source_id=source_id, source_data=source_data):
        raise HTTPException(status_code=404, detail="Source not found")
    return await update_source(db=db, source_id=source_id, source_data=source_data)

@router.delete("/{source_id}", status_code=status.HTTP_200_OK)
async def delete_job_source(source_id: str, db: AsyncSession = Depends(get_db)):
    if not await delete_source(db=db, source_id=source_id):
        raise HTTPException(status_code=404, detail="Source not found")
    return await delete_source(db=db, source_id=source_id)