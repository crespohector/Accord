FROM node:12 AS build-stage

WORKDIR /react-app
COPY react-app/. .

RUN npm install
RUN npm run build

FROM python:3.8

ARG FLASK_APP
ARG FLASK_ENV
ARG DATABASE_URL
ARG SCHEMA
ARG SECRET_KEY
ARG REACT_APP_BASE_URL

ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY . .

RUN flask db upgrade
# RUN flask seed undo
RUN flask seed all

# Run flask environment
CMD gunicorn --worker-class eventlet -w 1 app:app
