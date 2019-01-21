from microbit import *

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)

'''
running_time 函数会在设备启动后返回毫秒数。

while running_time() < 10000: 这一行检查运行时间是否小于1万毫秒（10秒）。
如果是， 则属于事件执行范围，设备将会显示 Image.ASLEEP （睡眠）。 
像待办清单一样，请注意 while 语句下的缩进。

显然，若运行时间≥1万毫秒，则会显示 Image.SURPRISED。
原因是 running_time 不满足＜1万毫秒的条件， 
while 条件不成立。
在这种情况下，循环终止，程序将会继续执行 while 循环之后的代码块。 
看起来像是设备休眠10秒后，露出“惊喜”的表情。
'''