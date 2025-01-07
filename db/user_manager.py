from db.database import Session
from db.models import User


class UserManager:
    def __init__(self):
        self.session = Session()

    def add_user(self, email, position, location, job_type):
        user = User(email=email, position=position, location=location, job_type=job_type)
        self.session.add(user)
        self.session.commit()

    def delete_user(self, email, position, location):
        user = self.session.query(User).filter_by(email=email, position=position, location=location).first()
        if user:
            self.session.delete(user)
            self.session.commit()

    def user_exists(self, email, position, location):
        return self.session.query(User).filter_by(email=email, position=position, location=location).count() > 0

    def get_all_users(self):
        return self.session.query(User).all()
