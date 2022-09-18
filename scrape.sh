#!/bin/sh
docker run --rm -w /app -it -v ${PWD}/app:/app kengo-k/pyscraping:v1.0.0 python /app/main.py $@