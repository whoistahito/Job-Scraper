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
