from microbit import *
while True:
    if button_a.is_pressed():
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
    else:
        display.show(Image. HEART)
        display.clear()

'''
这节课学习按键实验，让我们制做一个非常简单的micro:bit游戏。
当我们按下A键时，micro:bit点阵就会显示一个箭头指向A键；
当我们按下B键，micro:bit就会显示一个箭头指向B键；如果没有按键按下，micro:bit则显示一颗爱心。

判断按键是否被按下我们可以用button_a.is_pressed()这句函数来实现，也可以用button_a.was_pressed()。但是这两句函数也是有区别的，button_a.is_pressed()

表示按键是否正被按下；button_a.was_pressed()表示按钮自上次状态监测到当前是否被按下过 ；而button_a.get_presses()表示函数返回之前A按下的次数。调用这个函数后，计数会清零，重新开始计数。

 

逻辑解析：

if ...:  如果...事件是正确的或者发生了
       # do one thing  执行这条命令
elif ...:  否则如果...事件是正确的或者发生了
       # do another thing  执行这条命令
else:  否则
       # do yet another thing执行这条命令

 

所以这段函数的意思是：如果按键A被按下，micro:bit点阵显示开心，
如果按键B被按下,micro:bit点阵显示难过，否则micro:bit点阵显示一颗爱心。
'''