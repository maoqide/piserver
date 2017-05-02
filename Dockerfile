FROM maoqide/rpi-gpio

WORKDIR /piserver
EXPOSE 15000

RUN pip install Flask
ADD . /piserver
ENTRYPOINT ["python", "server.py"]

