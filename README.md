# api1_recipe_app

Learn API with DJANGO

CLONE THE PROJECT

> > git clone https://github.com/RAZAFINDRABEMISOMAcopertinot/api1_recipe_app.git .

BUILD A CONTAINER

> > docker build .

BUILD A DOCKER-COMPOSE IMAGE

> > docker-compose build

CREATE A DJANGO PROJECT

> > docker-compose run app sh -c "django-admin startproject app ."

CREATE A DJANGO APP

> > docker-compose run app sh -c "django-admin startapp core"

RUN A DJANGO TEST

> > docker-compose run app sh -c "python manage.py test"

> > docker-compose run app sh -c "python manage.py test && flake8"

MAKE MIGRATIONS DJANGO

> > docker-compose run app sh -c "python manage.py makemigrations core"

MIGRATE A MIGRATION

> > docker-compose run app sh -c "python manage.py migrate core"
