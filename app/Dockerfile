FROM tiangolo/uwsgi-nginx:python3.6-alpine3.8
MAINTAINER Giuseppe Broccolo <g.broccolo.7@gmail.com>

# replace the uwsgi plugin for Python 3.6
RUN apk --no-cache add build-base gcc gfortran linux-headers pcre-dev &&\
    pip3 install --no-cache-dir uwsgi==2.0.17.1

COPY ./requirements.txt /source/
COPY ./main.py /app/
COPY ./uwsgi_flask_nginx/uwsgi_timeout.conf /etc/nginx/conf.d/
COPY ./uwsgi_flask_nginx/nginx.conf /etc/nginx/
COPY ./supervisord/supervisord.ini /etc/supervisor.d/

RUN cd /source &&\
    pip install --no-cache-dir -r requirements.txt &&\
    cd / &&\
    rm -rf /source
