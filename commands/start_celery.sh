#!/bin/bash

rm srv/project/run/celery.pid
celery -A news_board worker -l info --workdir=/srv/project/src --pidfile=/srv/project/run/celery.pid
