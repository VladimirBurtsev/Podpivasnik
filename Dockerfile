FROM python:3.9

RUN mkdir -p /usr/src/bot

WORKDIR /usr/src/bot

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python","Bot.py"]

