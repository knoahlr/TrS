"""
WSGI config for Tr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from sys import path

from django.core.wsgi import get_wsgi_application

# def application(environ, start_response):
#     status = '200 OK'
#     output = b'Hello World!'

#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)

#     return [output]
path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["DJANGO_SETTINGS_MODULE"] = "TrDisplay.settings"

application = get_wsgi_application()
