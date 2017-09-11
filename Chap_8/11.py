import image

def double_photo(filename):
    img=image.Image(filename)
    newimg=image.EmptyImage(2*img.getWidth(),2*img.getHeight())
    img.setDelay(0)

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p=img.getPixel(col,row)
            newimg.setPixel(2*col,2*row,p)
            newimg.setPixel(2*col,2*row+1,p)
            newimg.setPixel(2*col+1,2*row,p)
            newimg.setPixel(2*col+1,2*row+1,p)
    return newimg

img=image.Image('luther.jpg')
win=image.ImageWin(2*img.getWidth(),2*img.getHeight())
newimg=double_photo("luther.jpg")
newimg.draw(win)
win.exitonclick()