
FROM python:3.9.1
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN chmod a+x entrypoints/django.sh

