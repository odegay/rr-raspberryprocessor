FROM rr-rpi-proc-core

RUN git clone https://github.com/odegay/rr-raspberryprocessor.git

WORKDIR rr-raspberryprocessor/src/client

RUN pip3 install -r requirements.txt

EXPOSE 8765

CMD [ "python3", "robotprocessor.py", "--host=0.0.0.0"]