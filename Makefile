build:
	docker build -t kengo-k/pyscraping:v1.0.0 .

test:
	docker run --rm -w /app -it -v ${PWD}/app:/app kengo-k/pyscraping:v1.0.0 python -m unittest