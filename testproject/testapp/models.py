from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Table,
)
from ..settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Entity(Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(20))

metadata= Base.metadata
