from sqlalchemy.orm import Session

from schemas.news import NewsCreate
from db.models.news import News


def create_new_news(news:NewsCreate,db:Session,writer_id:int):
    news_object = News(**news.dict(),writer_id=writer_id)
    db.add(news_object)
    db.commit()
    db.refresh(news_object)
    return news_object