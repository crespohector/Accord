# Build React App

FROM node:14 AS build-stage

ARG REACT_APP_BASE_URL
ENV REACT_APP_BASE_URL=$REACT_APP_BASE_URL

WORKDIR /react-app
COPY react-app/. .

RUN npm install
RUN npm run build

# Build Flask App
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

COPY . .
# Copy built React app from previous stage
COPY --from=build-stage /react-app/build/* app/static/

RUN pip install -r requirements.txt
RUN pip install psycopg2

# run flask migrations
RUN flask db upgrade
RUN flask seed undo
RUN flask seed all

# Run flask environment
CMD gunicorn --worker-class eventlet -w 1 app:app
