FROM python:latest

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python main.py"]
