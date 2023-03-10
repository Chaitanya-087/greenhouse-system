import RPi.GPIO as GPIO
import time
# import requests

# WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

#calculates distance
def distance(TRIG_PIN,ECHO_PIN):
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        startTime = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        stopTime = time.time()

    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34000) / 2
    return distance

#takes pins {echo,trig}
def sense(**kwargs):
    dist = distance(kwargs['trig_pin'],kwargs['echo_pin'])
    total = 12
    percent = (total - dist) / total
    percent = int(percent * 100)
    if percent >= 0:
        print("percentage of water level", percent)
    # iot code
    # res = requests.request('POST', 'https://api.thingspeak.com/update', params={
    #                         'api_key': WRITE_API_KEY}, data={'field4': percent})
    