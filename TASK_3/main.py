from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5.uic import loadUi
import pydicom as dicom
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PIL import Image
import math
import numpy as np

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        rotateAngle=''
        self.shearAngle=''
        self.oldRotatedImg=[]
        self.image=[]
        loadUi('interface.ui', self)
        self.ConstructButton.clicked.connect(self.constructT)
        self.RotateButton.clicked.connect(self.rotate)
        self.ShearButton.clicked.connect(self.shear)
        self.figureShow = plt.figure()
        self.canvas = FigureCanvas(self.figureShow)
        self.verticalLayout.addWidget(self.canvas)

    def constructT(self):
        self.tArr = np.zeros( (128,128))
        self.tArr[28:49,28:99] = 255
        self.tArr[48:99,53:74] = 255
        self.image =self.tArr
        plt.imshow(Image.fromarray(self.tArr))
        plt.axis('on')
        self.canvas.draw()

    def rotate(self):
        if len(self.image)==0: return self.displayError("Construct the image first")
        self.oldRotatedImg=self.image
        rotateAngle=int(self.RotateEdit.text())
        if not rotateAngle: self.displayError('Select a rotation angle')
        if self.comboBox.currentText()=='Clockwise':
            rotateAngle=math.radians(360-int(rotateAngle))
        else:
            rotateAngle=math.radians(int(rotateAngle))
        h=self.tArr.shape[0]
        w=self.tArr.shape[1]
        newH  = round(abs(h*math.cos(rotateAngle))+abs(w*math.sin(rotateAngle)))+1
        newW  = round(abs(w*math.cos(rotateAngle))+abs(h*math.sin(rotateAngle)))+1
        self.rotatedImg=np.zeros((newH,newW))
        centerH=round(((h+1)/2)-1)
        centerW=round(((w+1)/2)-1)
        newCenterH=round(((newH+1)/2)-1)
        newCenterW=round(((newW+1)/2)-1)

        for i in range(h):
            for j in range(w):
                y=h-1-i-centerH
                x=w-1-j-centerW
                newY=round(-x*math.sin(rotateAngle)+y*math.cos(rotateAngle))
                newX=round(x*math.cos(rotateAngle)+y*math.sin(rotateAngle))
                newY=newCenterH-newY
                newX=newCenterW-newX
                if 0<=newX < newW and 0<=newY<newH and newX>=0 and newY>=0:
                    self.rotatedImg[newY,newX]=self.oldRotatedImg[i,j]
        self.image=self.rotatedImg
        rotatedImage=Image.fromarray(self.rotatedImg)
        plt.imshow(rotatedImage)
        plt.axis('on')
        self.canvas.draw()
        return
    
    def shear(self):
        if len(self.image)==0: return self.displayError("Construct the image first")
        shearValue = (math.radians(int(self.ShearEdit.text())))
        shearedArr = np.zeros(self.tArr.shape)

        width = shearedArr.shape[0]
        height = shearedArr.shape[1]

        midX = width // 2
        midY = height // 2

        for i in range(height):
            for j in range(width):

                x = i 
                y = shearValue * (i - midX) + (j - midY)
                y = round(y) + midY

                if x >= 0 and y >= 0 and x < width and y < height:
                    shearedArr[i][j] = self.image[x][y]

        shearedImg = Image.fromarray(shearedArr)
        self.image= shearedArr
        plt.imshow(shearedImg)
        plt.axis('off')
        self.canvas.draw()
        return

    def displayError(self,e):
        error = QMessageBox()
        error.setIcon(QMessageBox.Critical)
        error.setWindowTitle('Error')
        error.setText('Error')
        error.setInformativeText(f"{e}")
        error.exec_()
        return





app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())