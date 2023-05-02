from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List 
from db.session import get_db
from db.models.news import News
from schemas.news import NewsCreate,ShowNews
from db.repo.news import create_new_news, retreive_news, list_news,update_news_by_id, delete_news_by_id

from db.models.users import User 
from apis.version1.route_users import get_current_user_from_token  

router = APIRouter()


@router.post("/create-news/",response_model=ShowNews)
def create_news(news: NewsCreate,db: Session = Depends(get_db)):
    current_user = 1
    news = create_new_news(news=news,db=db,writer_id=current_user)
    return news

@router.get("/get/{id}",response_model=ShowNews) # if we keep just "{id}" . it would stat catching all routes
def read_news(id:int,db:Session = Depends(get_db)):
    job = retreive_news(id=id,db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"News with this id {id} does not exist")
    return job

@router.get("/all",response_model=List[ShowNews]) 
def read_news(db:Session = Depends(get_db)):
    news = list_news(db=db)
    return news

@router.put("/update/{id}")  
def update_news(id: int,news: NewsCreate,db: Session = Depends(get_db)):
    current_user = 1
    message = update_news_by_id(id=id,news=news,db=db,writer_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"News with id {id} not found")
    return {"msg":"Successfully updated data."}


@router.delete("/delete/{id}")  
def delete_news(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    news = retreive_news(id =id,db=db)
    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"News with id {id} not found")
    if news.writer_id == current_user.id or current_user.is_superuser:
        delete_news_by_id(id=id,db=db,writer_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")
    