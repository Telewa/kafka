FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
WORKDIR /my_app
ADD . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt