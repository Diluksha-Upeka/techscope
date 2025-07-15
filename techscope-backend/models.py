from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    source = Column(String(255))
    url = Column(String(255))
    published_at = Column(DateTime, default=datetime.utcnow)
