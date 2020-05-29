#!/bin/bash

rm /srv/project/run/celerybeat.pid
rm /srv/project/run/celerybeat-schedule
celery -A news_board beat -l info --workdir=/srv/project/src --pidfile=/srv/project/run/celerybeat.pid  --schedule=/srv/project/run/celerybeat-schedule
