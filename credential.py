import os


class Credential:
    @staticmethod
    def get_email_address():
        return os.environ.get("email_address")

    @staticmethod
    def get_email_password():
        return os.environ.get("email_password")

    @staticmethod
    def get_google_api():
        return os.environ.get("google_api_key")

    @staticmethod
    def get_db_name():
        return os.environ.get("db_name")

    @staticmethod
    def get_db_password():
        return os.environ.get("db_password")

    @staticmethod
    def get_db_username():
        return os.environ.get("db_username")

    @staticmethod
    def get_db_uri():
        return "postgresql://%s:%s@127.0.0.1:5432/%s" % (
            Credential.get_db_username(), Credential.get_db_password(), Credential.get_db_name())
