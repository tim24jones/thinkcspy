import image
img=image.Image("luther.jpg")
newimg=image.EmptyImage(im.getWidth(),img.getHeight())
win=image.ImageWin()

for column in range(img.getWidth()):
	for row in range(img.getHeight()):
		p=img.getPixel(column,row)
		newpixel=image.Pixel(0,p.getGreen(),p.getBlue())
		img.setPixel(column,row,newpixel)
newimg.draw(win)
win.exitonclick()