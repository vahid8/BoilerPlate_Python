from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'

app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):
    return x + y

@app.task
def minus(x,y):
    return x - y

if __name__ == '__main__':
    print(add(2,4))