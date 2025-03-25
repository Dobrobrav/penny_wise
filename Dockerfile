FROM python:3.13

WORKDIR /usr/src/app

COPY /conf /usr/src/app/conf



RUN pip install -r conf/requirements.txt


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
