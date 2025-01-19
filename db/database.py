from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from db.models import Base

DATABASE_URL = "sqlite:///job_finder.db"

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)