from parents.models import Parent
from database import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship


class Child(Base):
    __tablename__ = "child_table"
    id = mapped_column(Integer, primary_key=True)
    height = mapped_column(Integer)
    parent_id = mapped_column(ForeignKey("parent_table.id"))
    parent = relationship("Parent", back_populates="child")