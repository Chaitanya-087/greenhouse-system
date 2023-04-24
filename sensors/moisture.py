import RPi.GPIO as GPIO
import time
import requests

WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

# takes pin{soil,pump}

def sense(**kwargs):
    status = GPIO.input(kwargs['soil_sen_pin'])
    print(status)
    res = requests.request('POST','https://api.thingspeak.com/update',params={'api_key':WRITE_API_KEY},data={'field3':status})
    if status == 0:
        print('water detected')
        print("pump state: off")
        GPIO.output(kwargs['pump_act_pin'],GPIO.LOW)

    if status == 1:
        print('no water detected')
        print("pump state: on")
        GPIO.output(kwargs['pump_act_pin'],GPIO.HIGH)



