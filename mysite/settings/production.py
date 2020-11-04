from .common import *
import os

# Use a separate file for the secret key
with open(os.path.join(BASE_DIR, 'secretkey.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 允许的服务器
ALLOWED_HOSTS = ['*']
