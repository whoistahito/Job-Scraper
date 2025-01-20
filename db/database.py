from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from db.models import Base
from credential import Credential

DATABASE_URL = Credential().get_db_uri()

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)