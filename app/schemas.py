from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class Records(BaseModel):
    id: int = 1000
    email: str
    first_name: str
    last_name: str
    driving_score: float
    age: int
    created_at: datetime
    updated_at: datetime


class ResponseModels(BaseModel):
    code: int = 0
    msg: str = ""
    limit: Optional[int] = 50
    offset: Optional[int] = 200
    records: List[Records]