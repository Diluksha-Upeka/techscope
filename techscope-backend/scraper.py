import requests
from bs4 import BeautifulSoup
from database import SessionLocal
from models import Article
from datetime import datetime
import re

SOFTWARE_KEYWORDS = [
    'software', 'developer', 'programming', 'engineer', 'coding', 'devops', 'backend', 'frontend', 'fullstack',
    'AI', 'ML', 'machine learning', 'data science', 'cloud', 'API', 'framework', 'library', 'algorithm', 'bug',
    'release', 'version', 'refactor', 'CI/CD', 'testing', 'agile', 'scrum', 'typescript', 'javascript', 'python',
    'java', 'c++', 'c#', 'go', 'rust', 'kotlin', 'swift', 'mobile', 'web', 'app', 'open source', 'repository',
    'github', 'gitlab', 'bitbucket'
]
def is_software_news(title):
    title_lower = title.lower()
    return any(re.search(r'\b' + re.escape(keyword.lower()) + r'\b', title_lower) for keyword in SOFTWARE_KEYWORDS)

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
        if is_software_news(article.title):
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
        if is_software_news(article.title):
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
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
    db.commit()
    db.close()

def scrape_wired():
    url = "https://www.wired.com/most-recent/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("li.archive-item-component a.archive-item-component__link")
    db = SessionLocal()
    for link in links[:10]:
        title = link.select_one("h2.archive-item-component__title")
        if not title:
            continue
        article = Article(
            title=title.text.strip(),
            source="Wired",
            url="https://www.wired.com" + link['href'],
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
    db.commit()
    db.close()

def scrape_ars_technica():
    url = "https://arstechnica.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("li.article a.overlay")
    db = SessionLocal()
    for link in links[:10]:
        title = link.get('aria-label')
        if not title:
            continue
        article = Article(
            title=title.strip(),
            source="Ars Technica",
            url=link['href'],
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
    db.commit()
    db.close()

def scrape_engadget():
    url = "https://www.engadget.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a[data-ylk*='slk:title']")
    db = SessionLocal()
    count = 0
    for link in links:
        title = link.text.strip()
        href = link.get('href')
        if not title or not href or not href.startswith('http'):
            continue
        article = Article(
            title=title,
            source="Engadget",
            url=href,
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
                count += 1
        if count >= 10:
            break
    db.commit()
    db.close()

def scrape_mashable():
    url = "https://mashable.com/tech"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a[data-ga-action='title']")
    db = SessionLocal()
    count = 0
    for link in links:
        title = link.text.strip()
        href = link.get('href')
        if not title or not href or not href.startswith('http'):
            continue
        article = Article(
            title=title,
            source="Mashable",
            url=href,
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
                count += 1
        if count >= 10:
            break
    db.commit()
    db.close()

def scrape_zdnet():
    url = "https://www.zdnet.com/topic/tech-industry/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.item-title")
    db = SessionLocal()
    count = 0
    for link in links:
        title = link.text.strip()
        href = link.get('href')
        if not title or not href or not href.startswith('http'):
            continue
        article = Article(
            title=title,
            source="ZDNet",
            url=href,
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
                count += 1
        if count >= 10:
            break
    db.commit()
    db.close()

def scrape_tnw():
    url = "https://thenextweb.com/section/tech"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.story-title")
    db = SessionLocal()
    count = 0
    for link in links:
        title = link.text.strip()
        href = link.get('href')
        if not title or not href or not href.startswith('http'):
            continue
        article = Article(
            title=title,
            source="The Next Web",
            url=href,
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
                count += 1
        if count >= 10:
            break
    db.commit()
    db.close()

def scrape_venturebeat():
    url = "https://venturebeat.com/category/tech/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.ArticleListing__title-link")
    db = SessionLocal()
    count = 0
    for link in links:
        title = link.text.strip()
        href = link.get('href')
        if not title or not href or not href.startswith('http'):
            continue
        article = Article(
            title=title,
            source="VentureBeat",
            url=href,
            published_at=datetime.utcnow()
        )
        if is_software_news(article.title):
            existing = db.query(Article).filter(Article.url == article.url).first()
            if not existing:
                db.add(article)
                count += 1
        if count >= 10:
            break
    db.commit()
    db.close()
