django-boilerplate
===============================================================================

ALPHA WIP!

Stack in mind:

*   Python 2.7.x
    * *NOT* Python 3 compatible (WIP)
*   Django 1.5+
*   Jinja2
*   LESS
*   Heroku

## Fresh Project Installation Instructions

*   Put django-boilerplate on pythonpath (todo: replace w/ real setup)
*   Create your project folder

        $ mkdir myproj
        $ cd myproj

*   Create a virtual environment (optional, but highly recommended)

        $ virtualenv ve
        $ source ve/bin/activate

*   Install django

        $ pip install django

*   Start a boilerplate project

        $ django-admin.py start_boilerplate_project --settings="boilerplate.conf.init_settings" <application_name>

*   Install requirements

        $ pip install -r requirements.txt

*   If all has gone well, you should be able to fire up the development server and see some example pages

        $ python manage.py runserver


## Integrate into an existing project

todo


