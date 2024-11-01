#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec python "/app/runner.py"
elif [ "$ENV" = 'PROD' ]; then
    echo "Running Production Server"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/runner.py \
         --callable app --stats 0.0.0.0:9191
elif [ "$ENV" = 'UNIT' ]; then
    echo "Running Unit Tests"
    exec python "/app/tests.py"
else
    echo "Unknown server startup parameter..."
fi