FROM python:3.6

WORKDIR /usr/app

ADD ./requirements.txt ./

RUN pip install -r requirements.txt

ADD ./ ./

CMD ["python3", "km_events.py"]
