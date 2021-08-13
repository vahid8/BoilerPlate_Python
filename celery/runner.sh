source ../../env/bin/activate
celery -A celery_tasks worker --loglevel=INFO
