import uuid
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime


class JobSourceCreate(BaseModel):
    name: str
    base_url: str
    is_active: bool = True


class JobSourceUpdate(BaseModel):
    name: Optional[str] = None
    base_url: Optional[str] = None
    is_active: Optional[bool] = None


class JobSourceResponse(BaseModel):
    id: uuid.UUID
    name: str
    base_url: str
    is_active: bool
    model_config = ConfigDict(from_attributes=True)