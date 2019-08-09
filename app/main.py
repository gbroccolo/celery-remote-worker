from traceback import format_exc
import os
from flask import Flask
from flask import request
from flask import json

from celery import Celery
from celery.result import AsyncResult
import celery.states as states


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


@app.route("/submit_task", methods=['POST'])
def submit():
    """
    Submit a new asynchronous job
    """

    param1 = int(request.form['param1'])
    param2 = int(request.form['param2'])

    args = [int(request.form['param1']), int(request.form['param2'])]

    task = celery.send_task('long_task', args=[param1, param2], kwargs={})

    return task.id, 200
    

@app.route('/check_tasks/<task_id>')
def check_task(task_id):
    """
    Check the status of all possibly finished tasks
    """

    res = celery.AsyncResult(task_id)
    if res.state==states.PENDING:
        return "still running", 202
    else:
        return str(res.result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
