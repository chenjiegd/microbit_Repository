from microbit import*
while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

'''
学习目标：

这节课学习单个引脚的使用，如果用鳄鱼夹夹住pin0引脚，鳄鱼夹的另一头夹住GND，则micro:bit点阵会显示一个笑脸，否则micro:bit点阵显示哭脸。

pin0.is_touched()函数表示pin0引脚是否被触摸，
这里可以理解为当一端连接GND的鳄鱼夹触碰到pin0引脚时，
表示pin0引脚被触摸，此时micro:bit点阵显示一个笑脸，否则micro:bit点阵显示哭脸。
'''