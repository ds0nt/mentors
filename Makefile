DOCKER_IMAGE_NAME = "docker-registry:5000/$(shell basename $(shell pwd))"

# install requirements
install:
	pip install -r requirements.txt

# freeze requirements
freeze:
	pip freeze > requirements.txt

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .
