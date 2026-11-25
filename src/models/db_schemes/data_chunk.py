from pydantic import BaseModel, Field,validator
from typing import Optional
from bson import ObjectId

class DataChunk(BaseModel):
    _id: Optional[ObjectId]
    chunk_itext:str = Field(...,min_length=1)
    chunk_metadata: Optional[dict] 
    chunk_order: int = Field(...,gt=0)
    chunk_project_id: ObjectId = Field(...,min_length=1)

    class Config:
        arbitrary_types_allowed = True