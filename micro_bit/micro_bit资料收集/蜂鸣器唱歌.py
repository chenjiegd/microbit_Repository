from microbit import *
import music
boat = Image("00090:90990:99990:90990:00090")
display.show(boat)
music.play(music.BIRTHDAY)

'''
学习目标：

这节课学习使用micro:bit机器人来播放音乐，机器人唱着生日快乐歌，同时点阵上显示一个蜂鸣器的的图案。

import是导入，这里的意思是导入music库函数，并从库里调用内置的music.NYAN旋律，下面是一个完整的旋律列表：

• music.DADADADUM
• music.ENTERTAINER

• music.PRELUDE
• music.ODE
• music.NYAN
• music.RINGTONE
• music.FUNK
• music.BLUES
• music.BIRTHDAY
• music.WEDDING
• music.FUNERAL
• music.PUNCHLINE
• music.PYTHON
• music.BADDY
• music.CHASE
• music.BA_DING
• music.WAWAWAWAA
• music.JUMP_UP
• music.JUMP_DOWN
• music.POWER_UP
• music.POWER_DOWN
'''