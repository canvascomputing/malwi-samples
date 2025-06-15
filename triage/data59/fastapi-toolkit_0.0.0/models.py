from sqlalchemy import (
    Column,
    Integer,
    String,
)

from fastapi_toolkit.db import BaseModel

__all__ = (
    'Book',
)


class Book(BaseModel):
    id = Column(Integer, primary_key=True)
    title = Column(String(length=42), nullable=False)
    page_amount = Column(Integer, nullable=False)
