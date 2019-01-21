from microbit import *
compass.calibrate()
while True:
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])

'''
学习目标：

这节课学习罗盘的使用，编好程序以后，下载到micro:bit，实现无论把micro:bit拿到哪个方位，micro:bit点阵上面的箭头都指向北方。

程序中首先调用compass.calibrate()函数进行罗盘校准，校准的过程是如图13-1把正中心的小红点在micro:bit点阵上描一个圈，
描完以后点阵上会出现一个笑脸，表示校准完成，接着显示一个箭头，无论你将micro:bit转到何方，箭头都是指向北方。
'''