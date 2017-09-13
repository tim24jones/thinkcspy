import image
import sys

sys.setExecutionLimit(200000) #may run long, so be patient

class matrix3_3:
    __init__(self,row0,row1,row2):
        self.r(0)=row0
        self.r(1)=row1
        self.r(2)=row2

    __str__(self):
        return([self.r0,self.r1,self.r2])        

    def getcol(self,n):
        if n>=0 and n<=2
            self.c(n)=row0[n]+row1[n]+row2[n]
        else:
            return 'row or column outside matrix limits'

    def multiply(self,othermatrix):

        for n in range(2):
            for i in range(2):
                self.r(n)[i]=self.r(n)*othermatrix.c(i)

    def sum_elements(self):
        sum=0
        for n in range(2):
            for i in range(2):
                sum=sum+self.r(n)[i]
        return sum

def sobol_operator(matrixA):
    Gx=matrix3_3([1,0,-1],[2,0,-2],[1,0,-1])
    Gy=matrix3_3([1,2,1],[0,0,0],[-1,-2,-1])
    sobol_value=sum_elements(multiply(Gx,matrixA))+sum_elements(multiply(Gy,matrixA))

    return sobol_value

def convolution(filename):
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
            if ((col and row)>0) and (col+1<img.getWidth()) and (row+1<img.getHeight()): #working with all but the edges first for simplicity
                for nearcol in range (col-1,col+2):
                    for nearrow in range (row-1,row+2):
                        nearp=img.getPixel(nearcol,nearrow)
                        greynearp=greyscale(nearp)
                        greypvalue=greynearp.getRed()
                        pixel_list[nearcol]=[pixel_list[nearcol]]+greynearp
                 nearmatrix=matrix_3_3(pixel_list[0],pixel_list[1],pixel_list[2])

def draw_image(filename):
    img=image.Image(filename)
    win=image.ImageWin(img.getWidth(),img.getHeight())
    img.setDelay(0)

                img.setPixel(col,row,newpixel)
            else:
                img.setPixel(col,row,oldpixel)
    img.draw(win)
    win.exitonclick()
     
def grayscale(pixel):
    newvalue=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())//3
    newpixel=image.Pixel(newvalue,newvalue,newvalue)
    return newpixel
    