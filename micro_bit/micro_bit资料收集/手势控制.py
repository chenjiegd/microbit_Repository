from microbit import *
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
      pin0.write_digital(1)
      pin1.write_digital(1)
      pin2.write_digital(1)
    elif gesture == "face down":
      pin0.write_digital(0)
      pin1.write_digital(0)
      pin2.write_digital(0)
    elif gesture == "left":
      pin0.write_digital(0)
      pin1.write_digital(0)
      pin2.write_digital(1)
    elif gesture == "right":
      pin0.write_digital(0)
      pin1.write_digital(1)
      pin2.write_digital(0)
    elif gesture == "down":
      pin0.write_digital(1)
      pin1.write_digital(0)
      pin2.write_digital(0)
    elif gesture == "up":
      pin0.write_digital(0)
      pin1.write_digital(1)
      pin2.write_digital(1)
    elif gesture == "freefall":
      pin0.write_digital(1)
      pin1.write_digital(1)
      pin2.write_digital(0)

'''
学习目标：

这节课学习手势控制，当我们下载好程序以后，握住micro:bit，
利用mirco:bit的重力感应实现做出不同的手势来控制灯的颜色以及亮和灭，
当我们把micro:bit拿起来并且点阵靠上时亮起由红绿蓝组成的白光，另外做不同的手势还能亮出红、绿、蓝等其他颜色。

程序中使用了while循环，使得程序一直处于逻辑判断中，不会停止。
如果手势是手心向上，使用手心朝上的手势，七彩灯亮白光，
使用手心朝下的手势，七彩灯灭掉，手心向左倾斜，七彩灯亮蓝光，手心向右倾斜，七彩灯亮绿光，手心向下倾斜，七彩灯亮红光，micro:bit做自由落地动作，七彩灯显示紫光。

micro：bit能够识别的手势有上、下、左、右、面朝下、面朝下，自由落体，3 g，6 g，8 g，摇。手势值的在程序中的表示依次是up, down, left, right, face up, face down,freefall, 3g, 6g, 8g, shake。
'''