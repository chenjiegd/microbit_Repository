from microbit import *
stop = Image("00900:09990:90909:09090:09090")
go = Image("00900:09990:90909:09090:90009")
while True:
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    display.show(stop)
    sleep(10000)
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)
    display.show(go)
    sleep(10000)


'''
学习目标：
这节课学习红绿灯实验，让我们制做一个非常简单的红绿灯游戏。用探照灯来模拟交通灯，当探照灯亮红色时，点阵上显示一个停止的人形图案，10秒以后探照灯变为绿色，点阵上显示一个行走的人形图案。

这节课简单的学习引脚的设置，我们把探照灯的R引脚连接pin0，就由pin0引脚来控制红灯的亮和灭，将探照灯的G引脚连接pin1，由pin1来控制绿灯的亮和灭，高电平亮灯，低电平灭。
'''