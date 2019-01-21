from microbit import *
display.show(Image.HEART)

'''

第一行的 from microbit import *在第一节已经讲过，意思是告诉MicroPython我们将要用到microbit库中的函数，from microbit import * 就是从microbit库中导入所有东西，在使用microbit的每个程序都要导入这个库。

第二行的 display.show(Image.HAPPY) 的意思是在micro:bit点阵上显示一个内置图像，display也是一个类似于microbit的库，只是它被包含在了microbit里面。display.show的意思就是使用display这个库里面的show()函数，这个函数的作用是显示一个内置图像，而这个内置的图像就是(Image.HEART)，一个心形图像，下面是一份内置图像的清单：

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

•Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.

CLOCK7, Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,Image.CLOCK1

•Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S,Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.XMAS

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE

Image.ALL_CLOCKS
Image.ALL_ARROWS

'''