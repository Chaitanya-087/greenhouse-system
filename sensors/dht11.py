import RPi.GPIO as GPIO
from .. import utils
import time
# import requests

# WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

# take pins {dht,humidifier}
def sense(**kwargs):
    DHT_sensor = utils.dht11.DHT11(pin=kwargs['dht_sen_pin'])  # config
    result = DHT_sensor.read()
    if result.is_valid():
        print(f'temperature:{result.temperature}C humidity:{result.humidity}%')
        # res = requests.request('POST','https://api.thingspeak.com/update' , params={'api_key' : WRITE_API_KEY} , data={'field1': result.temperature, 'field2': result.humidity})
        if result.temperature >= 32:
            GPIO.output(kwargs['fan_act_pin'], GPIO.HIGH)
        else:
            GPIO.output(kwargs['fan_act_pin'], GPIO.LOW)
    time.sleep(5)
