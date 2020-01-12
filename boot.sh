#!/bin/sh
echo Starting the engines!
exec gunicorn -b 0.0.0.0:$PORT --reload --access-logfile - --error-logfile - app:app
