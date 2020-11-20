"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 更改使用 WSGI协议时的配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')

application = get_wsgi_application()
