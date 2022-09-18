build:
	docker build -f dev/Dockerfile -t kengo-k/pyscraping:v1.0.0-dev .

release:
	docker build -f prd/Dockerfile -t kengo-k/pyscraping:v1.0.0 .

test:
	docker run --rm -it -v ${PWD}/app:/app kengo-k/pyscraping:v1.0.0-dev python -m unittest