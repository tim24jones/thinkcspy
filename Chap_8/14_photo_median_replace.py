import image
import sys
sys.setExecutionLimit(200000) #runs long, so be patient
def photo_median_replace(filename):
    img=image.Image(filename)
    win=image.ImageWin(img.getWidth(),img.getHeight())
    img.setDelay(0)
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p=img.getPixel(col,row)
            oldpixel=image.Pixel(p.getRed(),p.getGreen(),p.getBlue())
            nearred=0
            neargreen=0
            nearblue=0
            if ((col and row)>0) and (col+1<img.getWidth()) and (row+1<img.getHeight()): #smoothing all but the edges for simplicity
                for nearrow in range (col-1,col+2):
                    for nearcol in range (row-1,row+2):
                        nearp=img.getPixel(nearrow,nearcol)
                        nearred=nearred+0.13*nearp.getRed()
                        neargreen=neargreen+0.13*nearp.getGreen()
                        nearblue=nearblue+0.13*nearp.getBlue()
                newpixel=image.Pixel(nearred-0.13*p.getRed(),neargreen-0.13*p.getGreen(),nearblue-0.13*p.getBlue())
                img.setPixel(col,row,newpixel)
            else:
                img.setPixel(col,row,oldpixel)
    img.draw(win)
    win.exitonclick()

photo_median_replace("luther.jpg")
