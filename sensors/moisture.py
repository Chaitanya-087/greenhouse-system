import RPi.GPIO as GPIO
import time
# import requests

# WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

#takes pin{soil,pump}
def sense(**kwargs):
    status = abs(GPIO.input(kwargs['soil_sen_pin'])-1)
    # res = requests.request('POST','https://api.thingspeak.com/update',params={'api_key':WRITE_API_KEY},data={'field3':status})
    if status:
        print('water detected')
        GPIO.output(kwargs['pump_act_pin'],GPIO.LOW)
    else:
        print('no water detected')
        GPIO.output(kwargs['pump_act_pin'],GPIO.HIGH)
    time.sleep(5)
