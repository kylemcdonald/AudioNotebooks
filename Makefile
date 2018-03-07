build:
	docker build -t audionotebooks .

run: build
	docker run -it -p 8888:8888 audionotebooks