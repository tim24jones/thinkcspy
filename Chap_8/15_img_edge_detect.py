import cImage as image

def convolution(filename):
    img=image.Image(filename)
    win=image.ImageWin(img.getWidth(),img.getHeight())
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p=img.getPixel(col,row)
            oldpixel=image.Pixel(p.getRed(),p.getGreen(),p.getBlue())
            pixel_list=[]
            if ((col and row)>0) and (col+1<img.getWidth()) and (row+1<img.getHeight()): #working with all but the edges for simplicity
                for nearcol in range (col,col+2):
                    for nearrow in range (row,row+2):
                        nearp=img.getPixel(nearcol,nearrow)
                        greynearp=greyscale(nearp)
                        greypvalue=greynearp.getRed()
                        pixel_list=pixel_list+[greypvalue]
                    print('start',pixel_list,'end')
                nearmatrix=int(pixel_list[0])+int(pixel_list[1])*0-int(pixel_list[2])
                print(nearmatrix)
                outputpixel=image.Pixel(255-nearmatrix,255-nearmatrix,255-nearmatrix)
                #print(outputpixel)
                img.setPixel(col,row,outputpixel)
                #print(pixel_list)
            else:
                img.setPixel(col,row,oldpixel)
    img.draw(win)
    win.exitonclick()

def greyscale(pixel):
    newvalue=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())//3
    newpixel=image.Pixel(newvalue,newvalue,newvalue)
    return newpixel

#print(greyscale(image.Pixel(20,10,15)))
convolution('luther.jpg')
