import time
from sensors import dht11, moisture, ultrasonic
import RPi.GPIO as GPIO
import board
import adafruit_dht
# pin declaration
ULTRASONIC_TRIG_PIN = 18  # .
ULTRASONIC_ECHO_PIN = 24  # .
# DHT_SENSOR_PIN = 21  # .
FAN_ACT_PIN = 17  # .
SOIL_SENSOR_PIN = 4  # .
PUMP_ACT_PIN = 26  # .

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin setup
# GPIO.setup(DHT_SENSOR_PIN, GPIO.IN)
GPIO.setup(FAN_ACT_PIN, GPIO.OUT)
GPIO.setup(ULTRASONIC_TRIG_PIN, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)
GPIO.setup(SOIL_SENSOR_PIN, GPIO.IN)
GPIO.setup(PUMP_ACT_PIN, GPIO.OUT)

# off the relay since it's low active
GPIO.output(PUMP_ACT_PIN, GPIO.HIGH)
GPIO.output(FAN_ACT_PIN, GPIO.HIGH)


# dhtDevice = adafruit_dht.DHT11(board.D21, use_pulseio=False)


def read_dht_sensor():
    """
    Read temperature and humidity from DHT11 sensor
    """
    dht11.sense(fan_act_pin=FAN_ACT_PIN, GPIO=GPIO)


def read_moisture_sensor():
    """
    Read moisture level from soil moisture sensor
    """
    moisture.sense(soil_sen_pin=SOIL_SENSOR_PIN,
                   pump_act_pin=PUMP_ACT_PIN, GPIO=GPIO)


def read_ultrasonic_sensor():
    """
    Read distance from ultrasonic sensor
    """
    ultrasonic.sense(trig_pin=ULTRASONIC_TRIG_PIN,
                     echo_pin=ULTRASONIC_ECHO_PIN, GPIO=GPIO)


def run():
    try:
        while True:
            read_dht_sensor()
            time.sleep(1)
            print("************")

            read_moisture_sensor()
            time.sleep(1)
            print("************")

            read_ultrasonic_sensor()
            time.sleep(1)
            print("************")

    except KeyboardInterrupt:
        print('Terminated due to keyboard interrupt...')

    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    run()
