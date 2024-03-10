from pydantic import BaseModel


class ParentsChema(BaseModel):
    name: str
    age: int

    """class Config:
        orm_mode = True"""