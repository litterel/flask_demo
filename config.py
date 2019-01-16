#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/db_demo8'
SQLALCHEMY_DATABASE_URI = 'mysql://root:xuejianming@222.29.50.204/test_bbs'
SQLALCHEMY_TRACK_MODIFICATIONS = True


