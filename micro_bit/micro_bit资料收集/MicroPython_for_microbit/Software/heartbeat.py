# SparkFun Electronics
# Experiment 0.1
# Display an image

from microbit import *

beat1 = Image.HEART
beat2 = Image.HEART_SMALL
heartbeat = [beat1, beat2]
while True:
    display.show(heartbeat, delay=400)