
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /sources
WORKDIR /sources
COPY requirements.txt /sources/
RUN pip install -r requirements.txt
COPY . /sources/