NAME ?= costaki33

all: build run pull

build:
	docker build -t ${NAME}/meteorite-landings-data:1.0 .

run:
	docker run --name "meteorite-landings-data" -d -p 5031:5000 ${NAME}/meteorite-landings-data:1.0

redis:
	docker run -d -p 6431:6379 -v $(pwd)/data:/data:rw --name=costaki-redis redis:6 --save 1 1

pull:
	docker pull ${NAME}/meteorite-landings-data:1.0

clean:
	docker ps -a | grep costaki
