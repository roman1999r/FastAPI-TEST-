import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean


from core.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True,  unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime, default=datetime.datetime.now())
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
