"""
WSGI config for Tr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from sys import path

from django.core.wsgi import get_wsgi_application

path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["DJANGO_SETTINGS_MODULE"] = "{{ project_name }}.settings"

application = get_wsgi_application()
