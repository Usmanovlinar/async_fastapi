from pydantic import BaseModel


class ChildrenSchema(BaseModel):
    height: int
    parent_id : int

    class Config:
        orm_mode = True

class ChildrenRelatedSchema(BaseModel):
    height: int
    name : str
    age :int

