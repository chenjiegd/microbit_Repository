# Display random emotions on your bike.
# By Alex Glow; released to the public domain.

import radio
from microbit import display, Image, sleep

stop = Image("09990:"
             "90009:"
             "90009:"
             "90009:"
             "09990")
             
danger = Image("90909:"
             "90909:"
             "90909:"
             "00000:"
             "90909")
             
left = Image("00900:"
             "09000:"
             "99999:"
             "09000:"
             "00900")
             
right = Image("00900:"
             "00090:"
             "99999:"
             "00090:"
             "00900")
             
radio.on()

while True:
    incoming = radio.receive()
    if incoming == 'left':
        display.show(left)
        sleep(500)
    elif incoming == 'right':
        display.show(right)
        sleep(500)
    elif incoming == 'stop':
        display.show(stop)
        sleep(500)
    else:
        display.show(Image.HEART)
