import RPi.GPIO as GPIO

class moto():
    def __init__(self,out1,out2,out3,out4):
        print "moto init..."
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.__setup()

    def __setup(self):
        GPIO.setup(self.out1, GPIO.OUT)
        GPIO.setup(self.out2, GPIO.OUT)
        GPIO.setup(self.out3, GPIO.OUT)
        GPIO.setup(self.out4, GPIO.OUT)

    def stop(self):
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 0)

    def forward(self):
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 1)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 1)

    def backward(self):
        GPIO.output(self.out1, 1)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 1)
        GPIO.output(self.out4, 0)

    def right(self):
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 1)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 0)

    def left(self):
        GPIO.output(self.out1, 0)
        GPIO.output(self.out2, 0)
        GPIO.output(self.out3, 0)
        GPIO.output(self.out4, 1)

