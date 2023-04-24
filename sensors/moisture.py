import time
import requests

WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

# takes pin{soil,pump,GPIO}


def sense(**kwargs):
    GPIO = kwargs['GPIO']
    status = GPIO.input(kwargs['soil_sen_pin'])
    res = requests.request('POST', 'https://api.thingspeak.com/update',
                           params={'api_key': WRITE_API_KEY}, data={'field3': status})
    if status:
        print('no water detected')
        print("pump state: on")
        GPIO.output(kwargs['pump_act_pin'], GPIO.LOW)

    else:
        print('water detected')
        print("pump state: off")
        GPIO.output(kwargs['pump_act_pin'], GPIO.HIGH)
