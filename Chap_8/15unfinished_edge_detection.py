import image
import sys

sys.setExecutionLimit(200000) #may run long, so be patient

class matrix:
    def __init__(self,element_list):
        self.matrix=element_list
        self.rows=len(element_list)
        self.cols=self.get_cols()
        self.element_list=element_list

    def __str__(self):
        for n in range(len(self.element_list)):
            display_str=display_str+self.element_list[n]+'/n'
        return display_str

    def get_rows(self):
        return len(self.element_list)

    def get_cols(self):
        for n in range(self.rows-1):
            if len(self.matrix[n])!=len(self.matrix[n+1]):
                self.cols='Error, mismatched rows'
        return len(self.matrix[n])

    def get_row(self,row):
        return self.element_list[row]

    def get_col(self,col):
        column=[]
        for n in range(self.get_rows()):
            column=column+[self.element_list[n][col]]
        return column

    def get_element(self,row,col):
        return self.element_list[row][col]

    def add(self,other_matrix):
        if self.rows!=other_matrix.rows or self.cols!=other_matrix.cols:
            return 'Error, dimensions do not match for addition'
        else:
            output_matrix=[]
            for n in range(self.rows):
                current_row=[]
                for m in range(self.cols):
                    current_row=current_row+[int(self.element_list[n][m])+int(other_matrix.element_list[n][m])]
                output_matrix=output_matrix+current_row
        return output_matrix

    def subtract(self,other_matrix):
        if self.rows!=other_matrix.rows or self.cols!=other_matrix.cols:
            return 'Error, dimensions do not match for subtraction'
        else:
            output_matrix=[]
            for n in range(self.rows):
                current_row=[]
                for m in range(self.cols):
                    current_row=current_row+[int(self.element_list[n][m])-int(other_matrix.element_list[n][m])]
                output_matrix=output_matrix+current_row
        return output_matrix

    def multiply(self,other_matrix):
        output_matrix=[]
        for i in range(self.rows):
            for n in range(other_matrix.cols):
                current_row=[]
                for n in range(self.cols):
                    new_element=self.element_list[m][n]*other_matrix.element_list[n][i]
                    current_row=current_row+new_element
            output_matrix=output_matrix+current_row
        return output_matrix

    def avg_of_elements(self):#changed to average
        for m in range(self.rows):
            for n in range(self.cols):
                sum=sum+self.element_list[m][n]
        sum=sum//9
        return sum

def sobol_operator(matrixA):
    if matrixA.rows!=2 or matrixA.cols!=2:
        return 0
    else:
        Gx=matrix([1,0,-1],[2,0,-2],[1,0,-1])
        Gy=matrix([1,2,1],[0,0,0],[-1,-2,-1])
        xmult=matrixA.multiply(Gx)
        ymult=matrixA.multiply(Gy)
        sobol_value=xmult.avg_of_elements()+ymult.avg_of_elements()
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
                nearmatrix=matrix([[pixel_list[0]],[pixel_list[1]],[pixel_list[2]]])
                outputpixel=image.Pixel(sobol_operator(nearmatrix),sobol_operator(nearmatrix),sobol_operator(nearmatrix))
                img.setPixel(col,row,outputpixel)
            else:
                img.setPixel(col,row,oldpixel)
    img.draw(win)
    win.exitonclick()

def greyscale(pixel):
    newvalue=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())//3
    newpixel=image.Pixel(newvalue,newvalue,newvalue)
    return newpixel
    
convolution('luther.jpg')
