"""
WSGI config for battlesnake project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/opt/bitnami/projects/battlesnake')
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('PYTHON_EGG_CACHE', '/opt/bitnami/project/battlesnake/egg_cache')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'battlesnake.settings')

application = get_wsgi_application()
