from typing import Optional
from pydantic import BaseModel
from datetime import date,datetime


#shared properties
class NewsBase(BaseModel):
    title : Optional[str] = None
    thumbnail : Optional[str] = None
    description : Optional[str] = None
    date_posted : Optional[date] = datetime.now().date()
    
    

#this will be used to validate data while creating a Job
class NewsCreate(NewsBase):
    title : str
    thumbnail : str 
    description : str 
    
#this will be used to format the response to not to have id,owner_id etc
class ShowNews(NewsBase):
    title : str 
    description : Optional[str]
    date_posted : date
    is_approved : bool
    

    class Config():  #to convert non dict obj to json
        orm_mode = True