from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *


def copy_pic_into(smallpic,bigpic,start_x,start_y):
    for (x,y) in smallpic:
        color=smallpic.getColor(x,y)
        targetx=x+start_x
        targety=y+start_y
        bigpic.setColor(targetx,targety,color)
    bigpic.show()
    return bigpic



bigpic=Picture("../SampleImages/arches.jpg")
smallpic=Picture("../SampleImages/blueBird.jpg")

print(smallpic.width,smallpic.getHeight)
print(bigpic.width,bigpic.getHeight)
copy_pic_into(smallpic,bigpic,100,100)
keep_windows_open()