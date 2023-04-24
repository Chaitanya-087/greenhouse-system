from utils import dht11
import time
import requests
import adafruit_dht
import board

WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

# take pins {dht,humidifier,GPIO}
dhtDevice = adafruit_dht.DHT11(board.D21,use_pulseio=False)

def sense(**kwargs):
    try:
        GPIO = kwargs['GPIO']
        # dht_sensor = dht11.DHT11(pin=kwargs['dht_sen_pin'])  # config
        temperature,humidity = dhtDevice.temperature,dhtDevice.humidity
        if temperature and humidity:
            print(f'temperature:{temperature}C humidity:{humidity}%')
            res = requests.request('POST', 'https://api.thingspeak.com/update', params={
                                'api_key': WRITE_API_KEY}, data={'field1': temperature, 'field2': humidity})
            if temperature >= 29 and humidity >= 80:
                print("humidifier state: on")
                GPIO.output(kwargs['fan_act_pin'], GPIO.LOW)
            else:
                print("humidifier state: off")
                GPIO.output(kwargs['fan_act_pin'], GPIO.HIGH)
    except RuntimeError as error:
        pass