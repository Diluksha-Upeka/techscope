from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    source = Column(String(255))
    url = Column(String(255))
    published_at = Column(DateTime, default=datetime.utcnow)

class ArticleOut(BaseModel):
    id: int
    title: str
    source: str
    url: str
    published_at: Optional[datetime]

    class Config:
        orm_mode = True
