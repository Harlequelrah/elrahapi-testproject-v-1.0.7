from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from datetime import datetime

class EntityBaseModel(BaseModel):
    name:str=Field(example="the name of the entity")

class EntityCreateModel(EntityBaseModel):
    pass

class EntityUpdateModel(EntityBaseModel):
    pass

class EntityPatchModel(BaseModel):
    name: Optional[str]=Field(None, example="the updated name of the entity")

class EntityPydanticModel(EntityBaseModel):
    pass
    class Config:
        from_attributes=True


