import os
from random import random
from longtask import longtask

from flask import Flask
from celery import Celery


app = Flask(__name__)

# Celery backend is always the same
app.config['CELERY_RESULT_BACKEND'] = 'redis://%s:6379/0' % os.environ.get('REDIS_HOST')
app.config['CELERY_BACKEND_URL'] = 'redis://%s:6379/0' % os.environ.get('REDIS_HOST')
app.config['CELERY_ACCEPT_CONTENT'] = ['json']
app.config['CELERY_TASK_SERIALIZER'] = 'json'
app.config['CELERY_RESULT_SERIALIZER'] = 'json'
app.config['CELERY_IGNORE_RESULT'] = False
app.config['CELERY_TASK_RESULT_EXPIRES'] = 7500
app.config['CELERY_TRACK_STARTED'] = True
app.config['CELERY_HIJACK_ROOT_LOGGER'] = True

celery = Celery(
    'long_task',
    broker='redis://%s:6379/1' % os.environ.get('REDIS_HOST'))
celery.conf.update(app.config)


@celery.task(name='long_task')
def task(x, y):
    """
    The async, remote worker
    """

    return {'%s+%s' % (x, y): longtask.add(x, y)}
