"""
WSGI config for lp1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lp1.settings')

application = get_wsgi_application()
app = application



#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