from .base import *
import django_on_heroku
# Activate Django-Heroku.
django_on_heroku.settings(locals())
DEBUG = True