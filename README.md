1. ``pip install -r requirements.txt``
2. ``docker-compose up -d ``
3. ``python manage.py migrate``
4. ``python manage.py migrate --database djangoq``
5. ``python manage.py createcachetable``


PROD ``settings.py`` :
``EMAIL_BACKEND = 'django_q_email.backends.DjangoQBackend'``
sentry # https://sentry.io/organizations/akanza/issues/?project=5478154

TODO devops:
utworzenie kanału fcapp-sentry slack i podpięcie sentry
2 środowiska testowe (2 domeny) # master.(bierzączka)  staging.(rc) 

TODO Team:
git flow
branche
serwery testowe
definition of done
flow tasków
zasady współpracy
code review / approve etc.

TODO:
Adam - email dla fcappa
CORSy
allauth konfiguracja - placeholder for tests
gitlab ci - testy po każdym merge
sentry
pytest - testowy test
