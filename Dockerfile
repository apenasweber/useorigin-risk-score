FROM python:3.9-slim

COPY ./src /app/src
COPY ./requirements.txt /app
COPY . .

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000