from microbit import *
import neopixel

display.show(Image.HAPPY)

# 流水灯接在引脚pin16上，数量为3个
np = neopixel.NeoPixel(pin16, 3)

# 在流水灯中迭代每个LED
for pixel_id in range(0, len(np)):
    
    # 点亮第一个流水灯为红色
    np[0] = (255, 0, 0)
    
    # 显示颜色
    np.show()

'''
学习目标：

这节课学习使用Python编程点亮micro:bit机器人的流水灯。

import是导入，这里的意思是导入neopixel库函数，
首先让机器人显示一个笑脸，接着定义流水灯的引脚为pin16，数量为3个，
在流水等中迭代每个LED， np[0] = (255, 0, 0)表示点亮第一个流水灯为红色，
修改括号里的数值，可以点亮为其他颜色，最后显示我们点亮的颜色。
'''