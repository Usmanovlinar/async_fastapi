
from parents.models import Parent
from . import models, schemas
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Child


async def create_child(session: AsyncSession, child: schemas.ChildrenSchema):
    child = Child(**child.dict())
    session.add(child)
    await session.commit()
    await session.refresh(child)
    return child

async def get_child(session: AsyncSession, child_id: int):
    obj = await session.execute(select(Parent.name, Parent.age, Child.height,).join_from(Parent, Child).where(Child.id==child_id))

    return obj
def remove_child(session: AsyncSession, child_id: int):
    pass

