from microbit import *
fun1 = Image("00990:90900:99999:00909:09900")
fun2 = Image("99009:09099:00900:99090:90099")
all_fun = [fun1, fun2]
while True:
    if button_a.is_pressed():
      while True:
          pin0.write_digital(1)
          display.show(all_fun, delay=100)
    else:
      display.show(Image.HEART)
      display.clear()


'''
这节课学习使用Python语言编程使风扇电机转动起来，按下A键以后，风扇开始转动，同时点阵上有一个风扇转动的动画。

Micro:bit有5*5个LED组成的点阵，在点阵上的每个LED亮度都可以设置为0至9中的一个值。
如果一个LED的亮度被设置为0，那么它就熄灭了。如果如果它的亮度被设置为9，那么它就处于最亮的水平。
利用这个特点我们就可以在micro:bit点阵上显示自定义的风扇图像，
如果按键A按下，设置引脚pin0为高电平，搭配ULN2003驱动板来驱动风扇，同时点阵上显示一个风扇转动的动画。
'''