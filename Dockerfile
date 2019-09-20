FROM python:3.6-alpine3.10

LABEL Author="Suvorov Ilia <b31aim@yandex.ru>"

COPY . .

WORKDIR .

ENV TOKEN=YOUR_TOKEN

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev && \
    pip install --upgrade pip && \
    pip install --no-binary cryptography -r requirements.txt


CMD gunicorn --workers=1 --bind 0.0.0.0:5000  wsgi:app
