FROM python:3.8-alpine


RUN mkdir /app
RUN mkdir /app/templates

ADD password_provider.py /app
ADD requirements.txt /app
ADD templates /app/templates


WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080


CMD ["gunicorn", "-b 0.0.0.0:8080", "password_provider:app"]
