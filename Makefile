build:
	docker build -t tba .

run:
	docker run -p 5000:5000 --name tba_container tba:latest

build_run: build run

stop:
	docker stop tba_container

remove: stop
	docker rm tba_container

rebuild_run: remove build_run

test:
	docker run --rm tba python3 -m pytest