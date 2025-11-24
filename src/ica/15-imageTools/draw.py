from src.ica.helpers.imageTools import *
from src.ica.helpers.dummyWindow import *

def  draw_something():
    width=1000
    height=1000
    picture1=Picture(width,height)
    picture1.setAllPixels("pink")
    picture1.drawLine(width//2,50,width//2,200,"black")

    picture1.drawOval(10,10,20,15,"blue","yellow")
    picture1.show()
    return picture1


draw_something()
keep_windows_open()
from src.ica.helpers.dummyWindow import *
from src.ica.helpers.imageTools import *



def draw_something():
    new_pic=Picture(800,800)
    #center of circle head x=400, y=650 radius 50
    new_pic.drawOval(350,350,450,450,'black')
    new_pic.drawLine(400,450,400,600,color='black')
    new_pic.drawLine(400,600,300,750,color='black')
    new_pic.drawLine(400,600,500,750,color='black')
    new_pic.drawLine(300,525,500,525,color='black')
    return new_pic


def main():
    drawing = draw_something()
    drawing.show()

    keep_windows_open()


if __name__ == "__main__":
    main()