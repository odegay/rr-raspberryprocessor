FROM python:3.8-slim-buster


RUN git clone https://github.com/odegay/rr-raspberryprocessor.git

WORKDIR rr-raspberryprocessor

RUN pip3 install -r requirements.txt

EXPOSE 8765

CMD [ "python3", "robotprocessor.py", "--host=0.0.0.0"]