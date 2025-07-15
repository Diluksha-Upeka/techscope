import requests
from bs4 import BeautifulSoup
from database import SessionLocal
from models import Article
from datetime import datetime

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select(".titleline > a")

    db = SessionLocal()
    for link in links[:10]:
        article = Article(
            title=link.text,
            source="Hacker News",
            url=link['href'],
            published_at=datetime.utcnow()
        )
        # Avoid duplicates by checking title or URL
        existing = db.query(Article).filter(Article.url == article.url).first()
        if not existing:
            db.add(article)
    db.commit()
    db.close()

def scrape_theverge():
    url = "https://www.theverge.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("h2.c-entry-box--compact__title a")
    db = SessionLocal()
    for link in links[:10]:
        article = Article(
            title=link.text.strip(),
            source="The Verge",
            url=link['href'],
            published_at=datetime.utcnow()
        )
        existing = db.query(Article).filter(Article.url == article.url).first()
        if not existing:
            db.add(article)
    db.commit()
    db.close()

def scrape_techcrunch():
    url = "https://techcrunch.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.post-block__title__link")
    db = SessionLocal()
    for link in links[:10]:
        article = Article(
            title=link.text.strip(),
            source="TechCrunch",
            url=link['href'],
            published_at=datetime.utcnow()
        )
        existing = db.query(Article).filter(Article.url == article.url).first()
        if not existing:
            db.add(article)
    db.commit()
    db.close()
