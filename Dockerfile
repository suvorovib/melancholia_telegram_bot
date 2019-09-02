FROM python:3.6.5-alpine3.7 as base

LABEL Author="Suvorov Ilia <b31aim@yandex.ru>"

WORKDIR /app

#COPY --from=builder /app /usr/local
COPY . .


RUN apk update && \
    apk add --no-cache --virtual .build-deps && \
    apk add build-base && \
    apk add --no-cache libstdc++ postgresql-libs ca-certificates && \
    update-ca-certificates
    pip install --upgrade pip && \
    pip3 install --install-option="--prefix=/app" -r requirements.txt && \

EXPOSE 5000

CMD [ "python3", "run.py" ]