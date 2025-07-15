from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Article
from scraper import scrape_hackernews, scrape_theverge, scrape_techcrunch
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/articles")
def get_articles(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    articles = db.query(Article).order_by(Article.published_at.desc()).offset(skip).limit(limit).all()
    return articles

@app.api_route("/scrape", methods=["GET", "POST"])
def scrape(db: Session = Depends(get_db)):
    scrape_hackernews()
    scrape_theverge()
    scrape_techcrunch()
    return {"message": "Scraping done"}
