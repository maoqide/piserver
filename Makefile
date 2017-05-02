build:
	docker build -t maoqide/pi-motor .
run:
	docker run --privileged -d -p 15000:15000 maoqide/pi-motor
