FROM python:3.7.8-alpine3.12
# update to 3.8 when gevent support it

WORKDIR /app
COPY . .
RUN apk add --no-cache build-base && \
#    apk add --no-cache libffi-dev && \
    pip install -v -r requirements.txt && \
    chmod +x run.sh

CMD ./run.sh

