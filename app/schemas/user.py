# schemas/user.py
import uuid
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(min_length=8, max_length=72)  # max 72
    full_name: str | None = None
    years_experience: int | None = None
    location: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    email: EmailStr
    username: str
    full_name: str | None
    years_experience: int | None
    location: str | None
    salary_min: int | None
    salary_max: int | None
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"