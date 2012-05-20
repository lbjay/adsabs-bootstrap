from fabric.decorators import task
from fabric.context_managers import settings, hide
from fabric.colors import cyan
from utils import do

@task
def build():
    """Initialise and migrate database to latest version."""
    print(cyan('\nUpdating database...'))
    with settings(hide('warnings'), warn_only=True):
        do('venv/bin/alembic init db/postgresql')
