
from . import models, schemas
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Parent


async def create_parent(parent: schemas.ParentsChema, session: AsyncSession):
    obj = models.Parent(**parent.dict())
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj

async def get_parent(session: AsyncSession, parent_id: int):
    obj = await session.execute(select(Parent).where(Parent.id == parent_id))
    return obj.scalars().all()


async def remove_parent(session: AsyncSession, parent_id: int):
    result = await session.execute(delete(Parent).where(Parent.id == parent_id))
    await session.commit()
    return True




