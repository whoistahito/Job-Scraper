from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    email = Column(String, primary_key=True)
    position = Column(String, primary_key=True)
    location = Column(String, primary_key=True)
    job_type = Column(String, nullable=False)


class SentEmail(Base):
    __tablename__ = 'sent_email'
    user_email = Column(String, primary_key=True)
    job_url = Column(String, primary_key=True)
    position = Column(String, primary_key=True)
    location = Column(String, primary_key=True)
