FROM python:3.12-slim

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

LABEL maintainer=''
LABEL youtube=''
LABEL description='Development image for Real Estate Project'

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
&& apt-get install -y build-essential \
&& apt-get install -y libpq-dev \
&& apt-get install -y gettext \
&& apt-get install -y netcat-openbsd gcc postgresql \
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

#COPY ./requirements.txt /app/requirements.txt
#Check if requirements.txt is present
#RUN ls -l /app
#RUN pip3 install -r requirements.txt

COPY ./requirements.txt /app/requirements.txt
RUN ls -l /app  # Check if requirements.txt is present
RUN pip3 install -r requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint"]