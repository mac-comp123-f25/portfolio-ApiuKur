import random
import time
from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import Picture

red=random.randrange(0,255)
green=random.randrange(0,255)
blue=random.randrange(0,255)
color=(green,red,blue)
def get_rand_bg():
    pic2=Picture(100,100)
    pic2.setAllPixels(color)

    return pic2
    ...


def main():
    for i in range(10):
        pic = get_rand_bg()
        pic.show()
        time.sleep(1)

    keep_windows_open()


if __name__ == "__main__":
    main()
