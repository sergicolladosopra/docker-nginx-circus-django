FROM python:3.4
MAINTAINER sergicolladosopra@gmail.com

ENV PYTHONUNBUFFERED 1
RUN apt-get -y autoremove 
RUN apt-get update && apt-get install -y \
    nginx

RUN mkdir /code
WORKDIR /code

ADD requirements/common.txt /code/
ADD requirements/pre.txt /code/
ADD requirements/dev.txt /code/
RUN pip install -r common.txt
RUN pip install -r pre.txt
RUN pip install -r dev.txt

ADD docker /code/docker

RUN mkdir /code/config
ADD config/nginx.conf /code/config/

ADD config/circus.ini.tpl /code/config/
RUN envtpl /code/config/circus.ini.tpl --allow-missing --keep-template

CMD ["/code/docker/start.sh"]
EXPOSE 9999 8080
