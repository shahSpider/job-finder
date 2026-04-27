from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.db.session import get_db
from app.schemas.job import JobCreate, JobUpdate, JobResponse
from app.services.job_service import create_job_service, get_jobs_service, get_job_by_id_service, delete_job_service, update_job_service

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_job(job: JobCreate, db: AsyncSession = Depends(get_db)):
    return await create_job_service(db=db, job_data=job)

@router.get("/")
async def get_jobs(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=10),
    db: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * page_size
    return await get_jobs_service(page=page, page_size=page_size, offset=offset, db=db)

@router.get("/{job_id}", status_code=status.HTTP_200_OK)
async def get_job_by_id(job_id: str, db: AsyncSession = Depends(get_db)):
    if not await get_job_by_id_service(db=db, job_id=job_id):
        raise HTTPException(status_code=404, detail="Job not found")
    return await get_job_by_id_service(db=db, job_id=job_id)

@router.delete("/{job_id}", status_code=status.HTTP_200_OK)
async def delete_job(job_id: str, db: AsyncSession = Depends(get_db)):
    if not await delete_job_service(db=db, job_id=job_id):
        raise HTTPException(status_code=404, detail="Job not found")
    return await delete_job_service(db=db, job_id=job_id)

@router.put("/{job_id}", status_code=status.HTTP_200_OK)
async def update_job(job_id: str, job: JobUpdate, db: AsyncSession = Depends(get_db)):
    if not await update_job_service(db=db, job_id=job_id, job_data=job):
        raise HTTPException(status_code=404, detail="Job not found")
    return await update_job_service(db=db, job_id=job_id, job_data=job)