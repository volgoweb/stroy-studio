#!/bin/bash

python manage.py schemamigration helper --auto
python manage.py schemamigration page --auto
python manage.py schemamigration article --auto
python manage.py schemamigration building --auto
python manage.py schemamigration residence --auto
