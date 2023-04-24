import RPi.GPIO as GPIO
from utils import dht11
import time
import requests

WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

# take pins {dht,humidifier}
def sense(**kwargs):
    dht_sensor = dht11.DHT11(pin=kwargs['dht_sen_pin'])  # config
    result = dht_sensor.read()
    if result.is_valid():
        print(f'temperature:{result.temperature}C humidity:{result.humidity}%')
        res = requests.request('POST','https://api.thingspeak.com/update' , params={'api_key' : WRITE_API_KEY} , data={'field1': result.temperature, 'field2': result.humidity})
        if result.temperature >= 29 and result.humidity >= 80:
            print("humidifier state: on")
            GPIO.output(kwargs['fan_act_pin'], GPIO.HIGH)
        else:
            print("humidifier state: off")
            GPIO.output(kwargs['fan_act_pin'], GPIO.LOW)
