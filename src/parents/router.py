from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from parents import schemas, service

router = APIRouter(
    prefix="/parents",
    tags=["parents"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=201)
async def create_parent(parent: schemas.ParentsChema, session:AsyncSession =Depends(get_session)):
    response = await service.create_parent(parent, session)
    return response

@router.get("/{parent_id}", response_model=list[schemas.ParentsChema])
async def read_car(parent_id: int, session :AsyncSession =Depends(get_session)):
    response = await service.get_parent(session, parent_id)
    return [schemas.ParentsChema(name = c.name, age= c.age) for c in response]



@router.delete("/{car_id}")
async def delete_car(parent_id: int, session :AsyncSession =Depends(get_session)):
    response =  await service.remove_parent(session, parent_id)
    return response
