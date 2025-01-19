from db.database import Session
from db.models import User, SentEmail


class UserManager:
    def __init__(self):
        pass

    def add_user(self, email, position, location, job_type):
        with Session() as session:
            user = User(email=email, position=position, location=location, job_type=job_type)
            if not self.user_exists(email, position, location):
                session.add(user)
                session.commit()

    def delete_user(self, email, position, location):
        with Session() as session:
            user = self.user_exists(email=email, position=position, location=location)
            if user:
                session.delete(user)
                session.commit()

    def user_exists(self, email, position, location):
        with Session() as session:
            return (session.query(User)
                    .filter_by(email=email, position=position, location=location).one_or_none())

    def get_all_users(self):
        with Session() as session:
            return session.query(User).all()


class UserEmailManager:
    def __init__(self):
        pass

    def add_sent_email(self, email, job_url, position, location):
        with Session() as session:
            user = SentEmail(email=email, job_url=job_url, position=position, location=location)
            session.add(user)
            session.commit()

    def is_sent(self, email, job_url, position, location):
        with Session() as session:
            return session.query(SentEmail).filter_by(email=email, job_url=job_url, position=position,
                                                      location=location).count() > 0
