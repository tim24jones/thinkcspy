import image

def photo_to_bw(filename):
    img=image.Image(filename)
    win=image.ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)
    img.setDelay(0)
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p=img.getPixel(col,row)
            newvalue=(p.getRed()+p.getGreen()+p.getBlue())//3
            if newvalue>127:
                pixelvalue=255
            else:
                pixelvalue=0
            newpixel=image.Pixel(pixelvalue,pixelvalue,pixelvalue)
            img.setPixel(col,row,newpixel)
    img.draw(win)
    win.exitonclick()

photo_to_bw("luther.jpg")
