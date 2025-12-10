from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

pic = Picture(100, 100)
pic = Picture("../SampleImages/baldEagle.jpg")
pic.show()

def grayscale(pic):


    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = (r + g + b) / 3
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic


keep_windows_open()