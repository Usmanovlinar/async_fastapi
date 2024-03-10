from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import ForeignKey




class Parent(Base):
    __tablename__ = "parent_table"

    id = mapped_column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    child = relationship("Child", uselist=False, back_populates="parent")


