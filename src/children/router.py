from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from children import schemas, service
from database import get_session

router = APIRouter(
    prefix="/children",
    tags=["children"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.ChildrenSchema, status_code=201)
async def create_child(child: schemas.ChildrenSchema, session :AsyncSession =Depends(get_session)):
    return await service.create_child(session, child)

@router.get("/{child_id}")
async def get_child(child_id: int, session :AsyncSession =Depends(get_session)):
    """неправильно написан, не проходит валидацию при response_model"""
    """нужно переписать chemas скорее всего"""
    response = await service.get_child(session, child_id)
    return [schemas.ChildrenRelatedSchema(name=c.name, age=c.age, height = c.height) for c in response]



