"""
WSGI config for Ben10 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ben10.settings')

application = get_wsgi_application()
app = application