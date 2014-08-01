#!/bin/bash

python manage.py syncdb

python manage.py migrate --all

python manage.py loaddata foundation
python manage.py loaddata construction_type
python manage.py loaddata roof_covering
python manage.py loaddata article_category
python manage.py loaddata building
python manage.py loaddata residence
python manage.py loaddata work_type
python manage.py loaddata portfolio
