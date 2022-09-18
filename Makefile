build:
	docker build -t kengo-k/pyscraping:v1.0.0 .

run:
	docker run --rm -w /app -it -v ${PWD}/app:/app kengo-k/pyscraping:v1.0.0