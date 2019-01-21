from microbit import *

sleep(10000)
display.scroll(str(button_a.get_presses()))

# 睡眠1万毫秒（10秒），接着滚动显示按钮 A 被按下的次数。这就是全部了。