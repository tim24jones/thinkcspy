import image
def pixel_mapper(filename,map_function):
    img=image.Image(filename)
    img.setDelay(0)
    win=image.ImageWin(img.getWidth(),img.getHeight())
    
    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            imgp=img.getPixel(col,row)
            initialpixel=image.Pixel(imgp.getRed(),imgp.getGreen(),imgp.getBlue())
            newpixel=img.setPixel(col,row,map_function(initialpixel))
    img.draw(win)
    win.exitonclick()


def map_function(pixel):
    oldred=pixel.getRed()
    oldgreen=pixel.getGreen()
    oldblue=pixel.getBlue()
    newred=oldred*0.7
    newgreen=0
    newblue=oldblue*1.2
    return image.Pixel(newred,newgreen,newblue)
pixel_mapper("luther.jpg",map_function)
