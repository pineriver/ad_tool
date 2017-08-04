from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import datetime
from sqlalchemy import Column, Integer, String, Sequence, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from flask_login import UserMixin

class User(Base, UserMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    fb_user = relationship("Facebook", backref='facebook_ad')
    
class Facebook(Base):
   __tablename__ = "facebook_ad"
   
   id = Column(Integer, primary_key=True)
   ad_account = Column(String)
   page = Column(Integer)
   ad_name = Column(String(400))
   ad_bid = Column(Integer)
   ad_targeting = Column(String)
   start_time = Column(DateTime)
   end_time = Column(DateTime)
   ad_url = String()
   ad_title_1 = Column(String(50))
   ad_title_2 = Column(String(50))
   ad_body_1 = Column(String(90))
   ad_body_2 = Column(String(90))
   file_1 = Column(String)
   file_2 = Column(String)
   file_3 = Column(String)
    
Base.metadata.create_all(engine)