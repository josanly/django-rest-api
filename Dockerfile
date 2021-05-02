FROM python:3.9.3-alpine

ENV SERVICE=/srv/django_rest_api
ENV APP_USER=drf_api_user

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR "${SERVICE}"

COPY . ${SERVICE}

# setup dep
# install psycopg2 dependencies
RUN /bin/sh -c "set -e; \
                addgroup -S ${APP_USER} && adduser -S ${APP_USER} -G ${APP_USER} ; \
                mkdir -p ${SERVICE} ; \
                mkdir -p ${SERVICE}/static ; \
                apk update ; \
                apk add --virtual build-deps gcc python3-dev musl-dev ; \
                apk add postgresql-dev gcc python3-dev musl-dev ; \
                apk del build-deps ; \
                apk --no-cache add musl-dev linux-headers g++ ; \
                pip install --upgrade pip ; \
                pip install -r requirements.txt "

ENTRYPOINT ["python", "manage.py", "runserver"]
