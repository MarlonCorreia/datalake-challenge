FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir /src

WORKDIR /src
COPY . .

RUN pip install -r src/requirements.txt

ADD . /src/