FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir /src

WORKDIR /src
COPY . /src

RUN pip install -r requirements.txt

ADD . /src/