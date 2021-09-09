"""
WSGI config for npm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'npm.settings')

application = get_wsgi_application()

# for production

# import os
# import sys

# # assuming your django settings file is at '/home/rohaanmd/mysite/mysite/settings.py'
# # and your manage.py is is at '/home/rohaanmd/mysite/manage.py'
# path = '/home/rohaanmd/project-managemnet/npm'
# if path not in sys.path:
#     sys.path.append(path)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'npm.settings'

# # then:
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


