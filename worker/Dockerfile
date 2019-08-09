FROM python:3.6.8-alpine3.8
MAINTAINER Giuseppe Broccolo <g.broccolo.7@gmail.com>

# install supervisord
RUN apk update && apk add --no-cache supervisor

# install the custom library
COPY . /source
RUN cd /source &&\
    pip install --no-cache-dir . &&\
    cd / &&\
    rm -rf /source

# install the worker
RUN mkdir -p /app
COPY ./worker.py /app

# run the Celery worker through supervisor
COPY ./supervisord/supervisord.conf /etc/supervisord.conf
COPY ./supervisord/supervisord.ini /etc/supervisor.d/supervisord.ini
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
