from microbit import *
import random
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(str(random.randint(1, 6)))


'''
这节课学习随机函数，要求摇一摇micro:bit后，在micro:bit点阵上随机显示1至6中的一个数字。

import是导入，这里的意思是导入random库函数，变量gesture等于当前获取到的手势值，
如果当前的手势是"shake"，也就是摇一摇，那么将会在点阵上随机显示1至6中的一个数字。
'''