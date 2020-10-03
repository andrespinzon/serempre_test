FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

ADD . /test_serempre
WORKDIR /test_serempre

RUN pip install --upgrade pip

COPY requirements.txt /test_serempre/
RUN pip install -r requirements.txt
COPY . /test_serempre/