from fabric.api import run, env, sudo, cd, prefix

env.hosts = ['45.32.192.195']
env.user = 'jjspetz'

# below two need to be edited before deployment
DIR = '/home/jjspetz/django-exercise2'
VENV = 'source /home/jjspetz/.virtualenvs/dj-exercise2/bin/activate && source SECRETS.ENV'

def start ():
  with cd(DIR):
    with prefix(VENV):
      run('pm2 start uwsgi -- --ini uwsgi.ini > start.log')

def stop ():
  run('pm2 stop all > stop.log')

def deploy ():
  with cd(DIR):
    run('git pull')

    with prefix(VENV):
      run('pip install -r requirements.txt  > install.log')
      run('python manage.py migrate')

    run('pm2 restart all > restart.log')

def hello ():
  print("Hello")
