# piserver
control pi car

## This is my first flask app

## to start
```shell
# clone repository
git clone https://github.com/maoqide/piserver.git

cd piserver
python server.py
```
then you can access control your car on `ip:15000`

## docker
```shell
# run container
docker run --privileged -d -p 15000:15000 maoqide/pi-motor
```
then you can access control your car on `ip:15000` too.
