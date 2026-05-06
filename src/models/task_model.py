from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)