from src.ica.helpers.dummyWindow import keep_windows_open
from src.ica.helpers.imageTools import Picture


def simple_blend(pic1,pic2):
    width=pic1.getWidth()
    height=pic1.getHeight()

    #pic1=Picture(width,height)
    #pic2=Picture(width,height)
    newpic=Picture(width,height)
    for y in range(height):
        for x in range(width):
            (r,g,b)=pic1.getColor(x,y)
            (r1,g1,b1)=pic2.getColor(x,y)
            average = ((r + r1) // 2,
                       (g + g1) // 2,
                       (b + b1) // 2)
            newpic.setColor(x,y,average)
    newpic.show()
    return newpic
pic1=Picture("../SampleImages/bearLake.jpg")
pic2=Picture("../SampleImages/arches.jpg")
#newpic=Picture("../SampleImages/canadianRockies.jpg")
#simple_blend(pic1,pic2)

def simple_blend2(pic1,pic2):
    width=min(pic1.getWidth(),pic2.getWidth())
    height=min(pic1.getHeight(),pic2.getHeight())

    newpic=Picture(width,height)
    print(newpic.height,newpic.width)
    for y in range(height):
        for x in range(width):
            (r,g,b)=pic1.getColor(x,y)
            (r1,g1,b1)=pic2.getColor(x,y)
            average = ((r + r1) // 2,
                       (g + g1) // 2,
                       (b + b1) // 2)
            newpic.setColor(x,y,average)
    newpic.show()
    return newpic
pic1=Picture("../SampleImages/bearLake.jpg")
pic2=Picture("../SampleImages/blueBird.jpg")

def weighted_blend(pic1,pic2,wgt1):
    wg2=1-wgt1
    width=min(pic1.getWidth(),pic2.getWidth())
    height=min(pic1.getHeight(),pic2.getHeight())

    newpic=Picture(width,height)
    print(newpic.height,newpic.width)
    for y in range(height):
        for x in range(width):
            (r,g,b)=pic1.getColor(x,y)
            (r1,g1,b1)=pic2.getColor(x,y)
            average = ((wgt1 *r+wg2*r1) ,
                       (wgt1*g + wg2*g1) ,
                       (wgt1*b +wg2* b1) )
            newpic.setColor(x,y,average)
    newpic.show()
    return newpic
pic1=Picture("../SampleImages/bearLake.jpg")
pic2=Picture("../SampleImages/canyonlands.jpg")

weighted_blend(pic1,pic2,0.5)
weighted_blend(pic1,pic2,0.6)
def rotate_left(pic):
    w=pic.getWidth()
    h=pic.getHeight()
    newpic=Picture(h,w)
    for x in range(w):
        for y in range(h):
            (r,g,b)=pic.getColor(x,y)
            newx=y
            newy=w - x - 1
            newpic.setColor(newx,newy,(r,g,b))
    newpic.show()
    return newpic
pic=Picture("../SampleImages/arches.jpg")
rotate_left(pic)
pic.show()

def rotate_right(pic):

    w = pic.getWidth()
    h = pic.getHeight()
    newpic = Picture(h, w)
    for x in range(w):
        for y in range(h):
            (r, g, b) = pic.getColor(x, y)
            newx = h-y-1
            newy = x
            newpic.setColor(newx, newy, (r, g, b))
    newpic.show()
    return newpic

pic = Picture("../SampleImages/arches.jpg")
rotate_left(pic)
pic.show()



keep_windows_open()