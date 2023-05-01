from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.news import News
from schemas.news import NewsCreate,ShowNews
from db.repo.news import create_new_news

router = APIRouter()


@router.post("/create-news/",response_model=ShowNews)
def create_news(news: NewsCreate,db: Session = Depends(get_db)):
    current_user = 1
    news = create_new_news(news=news,db=db,writer_id=current_user)
    return news