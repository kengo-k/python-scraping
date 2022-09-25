build:
	docker build -f dev/Dockerfile -t kengokrbn/pyscraping:v1.0.0-dev .

release:
	docker build -f prd/Dockerfile -t kengokrbn/pyscraping:v1.0.0 .

test:
	docker run --rm -it -v ${PWD}/app:/app kengokrbn/pyscraping:v1.0.0-dev python -m unittest
