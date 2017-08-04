import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/ad_tool"
    DEBUG = True
    SECRET_KEY = os.environ.get("AD_TOOL_SECRET_KEY", "")
    