from extension import db


class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String, primary_key=True)
    position = db.Column(db.String, primary_key=True)
    location = db.Column(db.String, primary_key=True)
    job_type = db.Column(db.String, nullable=False)


class SentEmail(db.Model):
    __tablename__ = 'sent_email'
    email = db.Column(db.String, primary_key=True)
    job_url = db.Column(db.String, primary_key=True)
    position = db.Column(db.String, primary_key=True)
    location = db.Column(db.String, primary_key=True)
