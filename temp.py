import time
import random
import Adafruit_DHT
import RPi.GPIO as GPIO

PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)

sensor = Adafruit_DHT.DHT11

humidity, temperature = Adafruit_DHT.read(sensor, PIN, platform=Adafruit_DHT.DHT11)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')

# testing relay
# GPIO.output(PIN, GPIO.HIGH)

# val = random.choice([0, 1])

# try:
#     while 1:
#         print(val)
#         if (val):
#             GPIO.output(PIN, GPIO.LOW)
#         else:
#             GPIO.output(PIN, GPIO.HIGH)
#         time.sleep(2)

#         val = random.choice([0, 1])
        
# except KeyboardInterrupt:
#     GPIO.cleanup()
