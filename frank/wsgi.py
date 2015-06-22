"""
WSGI config for frank project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
#sys.path.append('/home/rameel/Development/Frankenstein')
#os.environ.setdefault("PYTHON_EGG_CACHE", "/home/rameel/Development/Frankenstein/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frank.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
