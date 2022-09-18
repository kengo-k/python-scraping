#!/bin/sh
docker run --rm -w /app -it kengo-k/pyscraping:v1.0.0 python /app/main.py $@