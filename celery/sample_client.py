from celery_tasks import add
for i in range(1000):
    add.delay(i,i)