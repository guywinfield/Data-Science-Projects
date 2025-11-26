FROM python:3.10-slim-buster

WORKDIR /todo-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT app:app"]