FROM python:3.6-alpine
MAINTAINER ivanpeng13@gmail.com

# Install python components to this docker instance
RUN apk update && apk add --no-cache \
    supervisor \
    sqlite

RUN mkdir -p /tmp
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY deployment/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /opt/wwc
ADD . /opt/wwc/craigslist-housing

WORKDIR /opt/wwc/craigslist-housing

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
#CMD ["python", "-m", "http.server"]