from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    page_amount: int

    class Config:
        orm_mode = True


class BookSchemaCreate(BaseModel):
    title: Optional[str] = None
    page_amount: Optional[int] = None
