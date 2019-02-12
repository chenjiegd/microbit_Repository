from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()

'''
这只宠物总是很悲伤，除非按下按钮 A。
如果按下按钮 B ，这只宠物会死掉。
（我意识到这不是一个令人愉快的游戏，所以也许你会想出改善这个游戏的方法。）
'''