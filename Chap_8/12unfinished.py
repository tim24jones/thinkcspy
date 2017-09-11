import image
import sys
sys.setExecutionLimit(60000)
def photo_smoothed(filename):
    img=image.Image(filename)
    win=image.ImageWin(img.getWidth(),img.getHeight())
    img.setDelay(0)
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p=img.getPixel(col,row)
            nearred=0
            neargreen=0
            nearblue=0
            if ((col and row)>0) and ((col,row)<(img.getWidth(),img.getHeight())): #smoothing all but the edges for simplicity
                for nearcol in range (col-1,col+1):
                    for nearrow in range (row-1,row+1):
                        nearp=img.getPixel(nearcol,nearrow)
                        nearred=0.1111*nearp.getRed()+nearred
                        neargreen=0.1111*nearp.getGreen()+neargreen
                        nearblue=0.1111*nearp.getBlue()+nearblue
                newpixel=image.Pixel(nearred,neargreen,nearblue)
                img.setPixel(col,row,newpixel)
            
            newR=(p.getRed()*0.393+p.getGreen()*0.769+p.getBlue()*0.189)
            newG=(p.getRed()*0.349+p.getGreen()*0.686+p.getBlue()*0.168)
            newB=(p.getRed()*0.272+p.getGreen()*0.534+p.getBlue()*0.131)
            newpixel=image.Pixel(newR,newG,newB)
            img.setPixel(col,row,newpixel)
    img.draw(win)
    win.exitonclick()

photo_smoothed("luther.jpg")