from sqlalchemy.orm import Session

from schemas.news import NewsCreate
from db.models.news import News


def create_new_news(news:NewsCreate,db:Session,writer_id:int):
    news_object = News(**news.dict(),writer_id=writer_id)
    db.add(news_object)
    db.commit()
    db.refresh(news_object)
    return news_object

def retreive_news(id:int,db:Session):
    item = db.query(News).filter(News.id == id).first()
    return item

def list_news(db:Session):
    items = db.query(News).all()
    return items

def update_news_by_id(id:int, news: NewsCreate,db: Session,writer_id):
    existing_news = db.query(News).filter(News.id == id)
    if not existing_news.first():
        return 0
    news.__dict__.update(writer_id=writer_id)  #update dictionary with new key value of writer_id
    existing_news.update(news.__dict__)
    db.commit()
    return 1


def delete_news_by_id(id:int,db: Session,writer_id):
    existing_news = db.query(News).filter(News.id == id)
    if not existing_news.first():
        return 0
    existing_news.delete(synchronize_session=False)
    db.commit()
    return 1