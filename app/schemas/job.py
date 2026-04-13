import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime

class JobCreate(BaseModel):
    title: str
    description: str
    company_name: str
    location: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: str

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    is_active: Optional[bool] = None

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    company_name: str
    location: str
    salary_min: Optional[int]
    salary_max: Optional[int]
    job_type: str
    source: str
    is_active: bool
    owner_id: int

    class Config:
        from_attributes = True