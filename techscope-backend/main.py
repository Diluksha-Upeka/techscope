from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Article, ArticleOut
from scraper import (
    scrape_hackernews, scrape_theverge, scrape_techcrunch, scrape_wired, scrape_ars_technica,
    scrape_engadget, scrape_mashable, scrape_zdnet, scrape_tnw, scrape_venturebeat
)
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scheduler = BackgroundScheduler()
scheduler.add_job(scrape_hackernews, 'interval', minutes=60)
scheduler.add_job(scrape_theverge, 'interval', minutes=60)
scheduler.add_job(scrape_techcrunch, 'interval', minutes=60)
scheduler.add_job(scrape_wired, 'interval', minutes=60)
scheduler.add_job(scrape_ars_technica, 'interval', minutes=60)
scheduler.add_job(scrape_engadget, 'interval', minutes=60)
scheduler.add_job(scrape_mashable, 'interval', minutes=60)
scheduler.add_job(scrape_zdnet, 'interval', minutes=60)
scheduler.add_job(scrape_tnw, 'interval', minutes=60)
scheduler.add_job(scrape_venturebeat, 'interval', minutes=60)
scheduler.start()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "TechScope API is running"}

@app.get("/articles", response_model=List[ArticleOut])
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).order_by(Article.published_at.desc()).all()
    return articles

@app.api_route("/scrape", methods=["GET", "POST"])
def scrape(db: Session = Depends(get_db)):
    scrape_hackernews()
    scrape_theverge()
    scrape_techcrunch()
    scrape_wired()
    scrape_ars_technica()
    scrape_engadget()
    scrape_mashable()
    scrape_zdnet()
    scrape_tnw()
    scrape_venturebeat()
    return {"message": "Scraping done"}
