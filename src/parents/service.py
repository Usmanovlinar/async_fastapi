from http.client import HTTPException

from parents import repository, schemas
from sqlalchemy.ext.asyncio import AsyncSession



def create_parent(parrent: schemas.ParentsChema, session: AsyncSession):
    return repository.create_parent(parrent, session)

async def get_parent(session: AsyncSession, parent_id: int):
    db_parent = await repository.get_parent(session, parent_id=parent_id)
    if db_parent is None:
        raise HTTPException(status_code=404)
    return db_parent;


def remove_parent(session: AsyncSession, parent_id: int):
    parent =  repository.get_parent(session,  parent_id=parent_id)
    if parent is None:
        raise HTTPException(status_code=404)
    return repository.remove_parent(session, parent_id)