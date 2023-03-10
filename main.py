import time
from . import sensors
import RPi.GPIO as GPIO
import time

#pin declaration
DHT_SEN_PIN = 21 #.
TRIG_PIN = 18 #.
ECHO_PIN = 24 #.
FAN_ACT_PIN = 18 #.
PUMP_ACT_PIN = 26 #.
SOIL_SEN_PIN = 4 #.

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pin setup
GPIO.setup(TRIG_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
GPIO.setup(SOIL_SEN_PIN,GPIO.IN)
GPIO.setup(FAN_ACT_PIN,GPIO.OUT)
GPIO.setup(PUMP_ACT_PIN,GPIO.OUT)

def run():
    try:
        while True:
            sensors.dht11.sense(fan_act_pin=FAN_ACT_PIN,dht_sen_pin=DHT_SEN_PIN)
            sensors.moisture.sense(soil_sen_pin=SOIL_SEN_PIN,pump_act_pin=PUMP_ACT_PIN)
            sensors.ultrasonic.sense(trig_pin=TRIG_PIN,echo_pin=ECHO_PIN)

    except KeyboardInterrupt:
        print('terminated due to keyboard interrupt...')
        GPIO.cleanup()

if __name__ == '__main__':
    run()
