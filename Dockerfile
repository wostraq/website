FROM python:3.5.2
RUN groupadd -g 1000 uwsgi && useradd -g uwsgi -u 1000 appuser
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
RUN mkdir /logs
WORKDIR /app
EXPOSE 8000
CMD gunicorn -b 0.0.0.0:8000 wsgi:app

