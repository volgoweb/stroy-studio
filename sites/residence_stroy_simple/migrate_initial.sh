#!/bin/bash

python manage.py syncdb

python manage.py schemamigration helper --initial
python manage.py schemamigration page --initial
python manage.py schemamigration article --initial
python manage.py schemamigration building --initial
python manage.py schemamigration residence --initial

