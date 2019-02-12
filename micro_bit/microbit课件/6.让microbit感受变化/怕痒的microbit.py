from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
        
'''
BBC micro:bit 上的每个引脚都由一个叫做 pinN 的 对象 表示，其中 N 是引脚号。
例如，若要用标记为0（零）的引脚进行操作，则需要使用名为 pin0 的对象。

用一只手通过引脚GND握住设备，
然后用另一只手触摸（或“胳肢”）引脚0（零）。
你应该看到显示屏从性情暴躁变为快乐！

这是一个非常基础的检测输入的方式。
然而，当你通过引脚插入电路或其他设备时，乐趣才真正开始。
'''