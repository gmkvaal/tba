build:
	docker build -t tba .

run:
	docker run -d -p 5000:5000 --name tba_container tba:latest

stop:
	docker stop tba_container

remove: stop
	docker rm tba_container

test:
	docker run --rm tba_container python3 -m pytest