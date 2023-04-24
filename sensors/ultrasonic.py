import time
import requests
from utils import mailService

WRITE_API_KEY = 'WRDR63RHQEBS6D6M'

# calculates distance


def distance(TRIG_PIN, ECHO_PIN, GPIO):
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2
    return distance


# takes pins {echo,trig}
def sense(**kwargs):
    dist = distance(kwargs['trig_pin'], kwargs['echo_pin'], kwargs['GPIO'])
    total = 12
    percent = (total - dist) / total
    percent = int(percent * 100)

    if percent >= 25:
        print(f"percentage of water level:{percent}%")
        # iot code
        res = requests.request('POST', 'https://api.thingspeak.com/update', params={
            'api_key': WRITE_API_KEY}, data={'field4': percent})

    elif percent >= 0 and percent < 25:
        print(f"low water level {percent}%")
        # send mail to user
        mailService.send_mail("sparkscj234@gmail.com", "--Water Level Alert--",
                              f"low water level: {percent}% need to refill ASAP!!!")
