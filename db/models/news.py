from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class News(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    thumbnail = Column(String,nullable=False)
    description = Column(String,nullable=False)
    date_posted = Column(Date)
    is_approved = Column(Boolean(),default=False)
    writer_id =  Column(Integer,ForeignKey("user.id"))
    writer = relationship("User",back_populates="news")
    
