FROM python:latest

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["waitress-serve", "--port=5000", "main:app"]
