PROJECT_ID = neat-resolver-286208
VERSION = v1
IMAGE_NAME = gcr.io/${PROJECT_ID}/tba:${VERSION}
CONTAINER_NAME = tba_container

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}

build_run: build run

stop:
	docker stop ${CONTAINER_NAME}

remove: stop
	docker rm ${CONTAINER_NAME}

rebuild_run: remove build_run

test:
	docker run --rm ${IMAGE_NAME} python3 -m pytest