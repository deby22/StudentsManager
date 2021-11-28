import os


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mysecretpassword@localhost:5432/template1"  # os.environ.get("SQLALCHEMY_DATABASE_URI")
