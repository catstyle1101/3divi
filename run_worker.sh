#!/bin/sh

until cd /app/
do
    echo "Waiting for server volume..."
done

# celery -A myproject worker --loglevel=info --concurrency 1 -E
celery -A myproject worker -P threads
