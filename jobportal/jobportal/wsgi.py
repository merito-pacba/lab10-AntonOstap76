import os
from django.core.wsgi import get_wsgi_application

env = os.getenv('DJANGO_ENV')

if env == 'production':
    settings_module = 'jobportal.deployment'
else:
    settings_module = 'jobportal.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()