import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime

class JobCreate(BaseModel):
    title: str
    description: str
    company: str
    location: str
    salary: Optional[int] = None
    url: str

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[int] = None
    url: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    company: str
    location: str
    salary: Optional[int]
    url: str

    class Config:
        from_attributes = True