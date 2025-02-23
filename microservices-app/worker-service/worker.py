from celery import Celery

app = Celery("worker", broker="redis://redis:6379/0")

@app.task
def process_data(data):
    return f"Processed: {data}"
