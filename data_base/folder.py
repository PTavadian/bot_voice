import datetime
import json
from sqlalchemy import Column, Integer, String
from data_base.create_db import Base



class Folders(Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True)
    folder_id = Column(String)
    title = Column(String)
    user_id = Column(String)
    user_date = Column(String)
    time = Column(String)


    def __init__(self, folder_id: str, title: str, user_id: str, user_date: dict=None):
        self.folder_id = folder_id
        self.title = title
        self.user_id = user_id
        self.user_date = json.dumps(user_date) 

        time = datetime.datetime.now()
        time = time.strftime("%d_%m_%Y__%H_%M_%S")
        self.time = time



