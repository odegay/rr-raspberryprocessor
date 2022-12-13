<h1>
    RASPBERRY PI PROCESSOR
</h1>

## Docker
docker build --no-cache -f Dockerfile_core -t rr-rpi-proc-core

## DEV
docker build --no-cache -f Dockerfile_dev . -t rr-rpi-proc

## PROD
docker build --no-cache -f Dockerfile_dev . -t rr-rpi-proc