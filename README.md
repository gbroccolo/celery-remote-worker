# celery-remote-worker
An example to setup some remote Celery workers that execute code installed only on server side

What is it trying to emulate?
-----------------------------

The idea is that we want to execute a function/method exposed by a certain library (let's think some
complex mathematical stuff...) that takes time. We would like to implement some microservice architecture
for this, that is able to get incoming requests into account and then it is able to enqueue all the tasks
in an async queue, that will be consumed by a remote worker. The idea then will be to have several workers
that are able to consume the queue concurrently and in parallel.

There is alarge amount of info in the web that is able to explain how to achieve this installing the library
both on app side (i.e. the microservice that ingest the requests) and worker side using a Celery decorator
in order to actually execute the code in the remote worker. Here we implement a solution that actually
need the library installed in the workers.

How to run the example
----------------------

Create a simple architecture with one app microservice and one worker based on docker, just running

```
$ docker-compose up -d
```

In order to run some example of enqueued requests:

```
$ curl -X POST -F "param1=2" -F "param2=12" http://localhost:5000/submit_task
7234a854-d3f6-4fe6-97ca-9082f9c55870

$ curl -X GET http://localhost:5000/check_tasks/7234a854-d3f6-4fe6-97ca-9082f9c55870
still runnning

$ curl -X GET http://localhost:5000/check_tasks/7234a854-d3f6-4fe6-97ca-9082f9c55870
{'2+12': 14}
```

Clean then the environment just with:

```
$ docker-compose down && docker rmi -f worker:latest app:latest
```
