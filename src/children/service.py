from http.client import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from children import schemas, repository


def create_child(session: AsyncSession, child: schemas.ChildrenSchema):
    return repository.create_child(session, child);

def get_child(session: AsyncSession, child_id: int):
    child = repository.get_child(session, child_id=child_id)
    if child is None:
        raise HTTPException(status_code=404)
    return child


def remove_child(session: AsyncSession, child_id: int):
    child = get_child(session, child_id=child_id)
    if child is None:
        raise HTTPException(status_code=404)
    return repository.remove_child(session, child)