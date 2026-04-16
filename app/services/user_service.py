from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate
import uuid

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(
        select(User).where(User.email == email)
    )
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(
        select(User).where(User.username == username)
    )
    return result.scalar_one_or_none()


async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user_in: UserCreate):
    hashed_password = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        username=user_in.username,
        full_name=user_in.full_name,
        years_experience=user_in.years_experience,
        location=user_in.location,
        salary_min=user_in.salary_min,
        salary_max=user_in.salary_max,
        password_hash=hashed_password
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user


async def authenticate_user(db: AsyncSession, email: str, password: str) -> User | None:
    user = await get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
 
async def update_user_password(
    db: AsyncSession,
    user_id: int,
    current_password: str,
    new_password: str
) -> bool:
    """
    Update user password after verifying current password
    
    Returns:
        bool: True if password updated successfully
    
    Raises:
        ValueError: If current password is incorrect
    """
    # Get user from database
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalar_one_or_none()
    
    if not user:
        raise ValueError("User not found")
    
    # Verify current password
    if not verify_password(current_password, user.hashed_password):
        raise ValueError("Current password is incorrect")
    
    # Hash and update new password
    user.hashed_password = hash_password(new_password)
    
    # Commit changes
    await db.commit()
    await db.refresh(user)
    
    return True
 