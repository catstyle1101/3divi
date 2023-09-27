FROM python:3.11-slim-buster

RUN apt-get update 
RUN apt-get install libpq-dev gcc cmake build-essential pkg-config ffmpeg libsm6 libxext6 -y
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install face-recognition==1.3.0
RUN pip install gunicorn
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD run_server.sh .
ADD run_worker.sh .
RUN chmod +x run_server.sh
RUN chmod +x run_worker.sh
ADD ./myproject/ .
