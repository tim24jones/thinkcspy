import image
import sys

sys.setExecutionLimit(200000) #may run long, so be patient

class matrix3_3:
    def __init__(self,row0,row1,row2):
        self.r0=row0
        self.r1=row1
        self.r2=row2
        self.c0=row0[0]+row1[0]+row2[0]
        self.c1=row0[1]+row1[1]+row2[1]
        self.c2=row0[2]+row1[2]+row2[2]

    def __str__(self):
        return([self.r0,self.r1,self.r2])        

    def multiply(self,othermatrix):

        output0_0=self.r0*othermatrix.c0
        output0_1=self.r0*othermatrix.c1
        output0_2=self.r0*othermatrix.c2
        output.r0=[output0_0,output0_1,output0_2]

        output1_0=self.r1*othermatrix.c0
        output1_1=self.r1*othermatrix.c1
        output1_2=self.r1*othermatrix.c2
        output.r1=[output1_0,output1_1,output1_2]
        
        output2_0=self.r2*othermatrix.c0
        output2_1=self.r2*othermatrix.c1
        output2_2=self.r2*othermatrix.c2
        output.r2=[output2_0,output2_1,output2_2]
        
        return matrix3_3(self,output.r0,output.r1,output.r2)

    def sum_elements(self):
        sum=0
        for n in range(2):
            sum=sum+self.r0[n]
            sum=sum+self.r1[n]
            sum=sum+self.r2[n]
        return sum

def sobol_operator(matrixA):
    Gx=matrix3_3([1,0,-1],[2,0,-2],[1,0,-1])
    Gy=matrix3_3([1,2,1],[0,0,0],[-1,-2,-1])
    xmult=matrixA.multiply(Gx)
    ymult=matrixA.multiply(Gy)
    sobol_value=xmult.sum_elements()+ymult.sum_elements()
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
            pixel_list=[]
            if ((col and row)>0) and (col+1<img.getWidth()) and (row+1<img.getHeight()): #working with all but the edges first for simplicity
                for nearcol in range (col-1,col+2):
                    for nearrow in range (row-1,row+2):
                        nearp=img.getPixel(nearcol,nearrow)
                        greynearp=greyscale(nearp)
                        greypvalue=greynearp.getRed()
                        pixel_list=pixel_list+[greypvalue]
                nearmatrix=matrix3_3(pixel_list[0],pixel_list[1],pixel_list[2])
                outputpixel=sobol_operator(nearmatrix)
    img.setPixel(col,row,outputpixel)
    img.draw(win)
    win.exitonclick()

#def draw_image(filename):
#    img=image.Image(filename)
#    win=image.ImageWin(img.getWidth(),img.getHeight())
#    img.setDelay(0)

#                img.setPixel(col,row,newpixel)
#            else:
#                img.setPixel(col,row,oldpixel)
#    img.draw(win)
#    win.exitonclick()
def greyscale(pixel):
    newvalue=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())//3
    newpixel=image.Pixel(newvalue,newvalue,newvalue)
    return newpixel
    
convolution('luther.jpg')
