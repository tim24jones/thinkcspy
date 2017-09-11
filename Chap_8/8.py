import image
img=image.Image("luther.jpg")
win=image.ImageWin(img.getWidth(),img.getHeight())
img.draw(win)
img.setDelay(0)

p=img.getPixel(45,55) #column 45, row 55

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p=img.getPixel(col,row)
        newvalue=(p.getRed()+p.getGreen()+p.getBlue())//3
        newpixel=image.Pixel(newvalue,newvalue,newvalue)
        img.setPixel(col,row,newpixel)
img.draw(win)
win.exitonclick()
