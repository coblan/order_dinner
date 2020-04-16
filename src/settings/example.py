from . base import *

import pymysql

pymysql.install_as_MySQLdb()
ALLOWED_HOSTS=['*']

DATABASES = {
     'default': {
        'NAME': 'order_dinner',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'zhou',
        'PASSWORD': 'zhou570508',
        'HOST': '172.18.215.159', 
        'PORT': '3306', 
        'OPTIONS': {'charset':'utf8mb4'},

      },
} 