# Display random emotions on your bike.
# By Alex Glow; released to the public domain.

import radio
from microbit import display, Image, button_a, button_b, sleep

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

cdbutt = 0 # Countdown from pressing 1 button, so it doesn't show arrow instead of stop sign.
cdstop = 0 # Countdown after displaying stop sign, so arrows don't display.
             
radio.on()

while True:
    cdstop = cdstop + 1
    
    if button_a.is_pressed() and button_b.is_pressed():
        cdstop = 0
        radio.send('stop')
        display.show(stop)
        sleep(500)
        display.clear()
        
    elif button_a.is_pressed() and cdstop >= 150 and cdbutt >= 150:
        radio.send('left')
        display.show(left)
        sleep(500)
        cdbutt = 0
        display.clear()
    elif button_a.is_pressed() and cdstop >= 150:
        cdbutt = cdbutt + 1
        
    elif button_b.is_pressed() and cdstop >=150 and cdbutt >= 150:
        radio.send('right')
        display.show(right)
        sleep(500)
        cdbutt = 0
        display.clear()
    elif button_b.is_pressed() and cdstop >= 150:
        cdbutt = cdbutt + 1
