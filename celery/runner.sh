source ../../env/bin/activate
celery  -A my_task worker --concurrency=1 --loglevel=INFO
