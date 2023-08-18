FROM python:3.10-alpine3.16
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev 
WORKDIR /app 
RUN pipenv shell
RUN pipenv install -r requirements.txt
COPY . .
RUN find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
RUN find . -path "*/migrations/__pycache__/*"  -delete
EXPOSE 8000
WORKDIR /app/phone_book
RUN python manage.py makemigrations 
RUN python manage.py migrate
ENTRYPOINT python manage.py runserver 0.0.0.0:8000