from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *
import random




def copy_pic_into(smallpic,bigpic):
    randomx=random.randrange(10)
    randomy=random.randrange(10)
    for (x,y) in smallpic:
        color=smallpic.getColor(x,y)
        targetx=x+randomx
        targety=y+randomy
        bigpic.setColor(targetx,targety,color)
    bigpic.show()
    return bigpic



bigpic=Picture("../SampleImages/arches.jpg")
smallpic=Picture("../SampleImages/blueBird.jpg")

copy_pic_into(smallpic,bigpic)
keep_windows_open()