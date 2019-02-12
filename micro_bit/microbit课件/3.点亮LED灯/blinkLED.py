# SparkFun Electronics
# Experiment 1.0
# Blinking an LED

from microbit import *

while True:
    pin0.write_digital(1)
    sleep(200)
    pin0.write_digital(0)
    sleep(200)