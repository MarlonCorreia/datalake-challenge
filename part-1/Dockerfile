FROM python:3

RUN mkdir /src

WORKDIR /src
COPY . .

RUN pip install -r src/requirements.txt

ADD . /src/