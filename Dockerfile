FROM python:alpine3.17

RUN apk add git

# RUN apk add py3-aiohttp

RUN set -ex && \
   apk add --no-cache gcc musl-dev

#RUN set -ex && \
#    rm -f /usr/libexec/gcc/x86_64-alpine-linux-musl/6.4.0/cc1obj && \
#    rm -f /usr/libexec/gcc/x86_64-alpine-linux-musl/6.4.0/lto1 && \
#    rm -f /usr/libexec/gcc/x86_64-alpine-linux-musl/6.4.0/lto-wrapper && \
#    rm -f /usr/bin/x86_64-alpine-linux-musl-gcj

RUN apk update

RUN git clone https://github.com/odegay/rr-raspberryprocessor.git

WORKDIR rr-raspberryprocessor/src/client

RUN pip3 install -r requirements.txt

EXPOSE 8765

CMD [ "python3", "robotprocessor.py", "--host=0.0.0.0"]