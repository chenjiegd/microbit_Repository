# author:五丝菜卷
# 2019/1/31
# 简易交通灯

from microbit import *


while True:
    # 绿灯亮10秒
    time0 = 10
    pin0.write_digital(1)
    while time0 > 0:
        if time0 == 10:
            display.scroll(str(time0))
        else:
            display.show(str(time0))
            sleep(1000)
        time0 = time0 - 1
    pin0.write_digital(0)

    # 黄灯亮3秒
    time1 = 3
    pin1.write_digital(1)
    while time1 > 0:
        display.show(str(time1))
        sleep(1000)
        time1 = time1 - 1
    pin1.write_digital(0)

    # 红灯亮10秒
    time0 = 10
    pin2.write_digital(1)
    while time0 > 0:
        if time0 == 10:
            display.scroll(str(time0))
        else:
            display.show(str(time0))
            sleep(1000)
        time0 = time0 - 1
    pin2.write_digital(0)