import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gameCatalog.settings')
django.setup()

def collect_static():
    call_command('collectstatic', '--noinput')

if __name__ == '__main__':
    collect_static()