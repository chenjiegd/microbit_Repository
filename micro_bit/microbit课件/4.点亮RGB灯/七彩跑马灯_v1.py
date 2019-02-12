from microbit import *
import neopixel
display.show(Image.HAPPY)
# 定义流水灯接在引脚pin16上，数量为3个
np = neopixel.NeoPixel(pin16, 3)
while True:
    for pixel_id in range(0, len(np)):
        np[0] = (255, 0, 0)
        np.show()
        sleep(200)
        np.clear()
        np[1] = (0, 255, 0)
        np.show()
        sleep(200)
        np.clear()
        np[2] = (0, 0, 255)
        np.show()
        sleep(200)
        np.clear()
        np[0] = (255, 255, 0)
        np.show()
        sleep(200)
        np.clear()
        np[1] = (0, 255, 255)
        np.show()
        sleep(200)
        np.clear()
        np[2] = (255, 0, 255)
        np.show()
        sleep(200)
        np.clear()


'''
学习目标：

这节课学习使用Python编程从左往右轮流点亮micro:bit机器人的流水灯。

import是导入，这里的意思是导入neopixel库函数，首先让机器人显示一个笑脸，
接着定义流水灯的引脚为pin16，数量为3个，
在流水等中迭代每个LED， np[0] = (255, 0, 0)表示点亮第一个流水灯为红色，
点亮后延时200毫秒，清除显示，点亮第二个灯，往下依次类推。
'''