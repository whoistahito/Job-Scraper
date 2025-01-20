import os


class Credential:
    def __init__(self):
        pass

    def get_email_address(self):
        return os.environ.get("email_address")

    def get_email_password(self):
        return os.environ.get("email_password")

    def get_google_api(self):
        return os.environ.get("google_api_key")

    def get_db_name(self):
        return os.environ.get("db_name")

    def get_db_password(self):
        return os.environ.get("db_password")

    def get_db_username(self):
        return os.environ.get("db_username")

    def get_conn_uri(self):
        return "postgresql://%s:%s@127.0.0.1:5432/%s" % (
        self.get_db_username(), self.get_db_password(), self.get_db_name())
