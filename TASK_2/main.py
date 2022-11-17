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
        self.grayScaledImgArr=[]
        self.path=''
        loadUi('interface.ui', self)
        self.figureShow = plt.figure()
        self.canvas_2 = FigureCanvas(self.figureShow)
        self.LayoutScale.addWidget(self.canvas_2)

        self.figureScale = plt.figure()
        self.canvas_1 = FigureCanvas(self.figureScale)
        self.LayoutShow.addWidget(self.canvas_1)

        

        self.actionBrowse.triggered.connect(self.openFileDialogue)
        self.ResizeButton.clicked.connect(lambda: self.convertToGrayScaleAndScale(True))
        self.ConvertButton.clicked.connect(self.displayGrayScaledImg)

    
    def openFileDialogue(self):
        self.path,_ = QFileDialog.getOpenFileName()
        self.suffix = self.path.split('.')[-1]
        if self.suffix=='dcm': self.openDicom()
        else: self.openImage()

    def openImage(self):
        try: 
            self.image = Image.open(self.path)
        except Exception as e: 
            self.displayError(e) 
            print(e)
        self.width = self.image.width
        self.height = self.image.height
        try: self.depth = math.ceil(math.log(np.amax(self.image) - np.amin(self.image) + 1, 2)) * np.shape(self.image)[2]
        except: self.depth = math.ceil(math.log(np.amax(self.image) - np.amin(self.image) + 1, 2))
        self.size = self.width * self.height * self.depth
        self.colorMode = self.image.mode
        self.ImageDim.setText(f"{self.height,self.width}")
        self.ImageColor.setText(f"{self.colorMode}")
        self.ImageSize.setText(f"{self.size}")
        self.BitDepth.setText(f"{self.depth}")
        self.PatientName.setText("None")
        self.PatientAge.setText("None")
        self.Modality.setText("None")
        self.BodyPart.setText("None")
        plt.imshow(self.image)
        plt.axis('off')
        self.canvas_1.draw()

    def openDicom(self):
        try:
            self.ds = dicom.dcmread(self.path)
            self.width =  self.ds.Columns 
            self.height =  self.ds.Rows 
            self.depth =  self.ds.BitsAllocated
            self.size = self.width * self.height * self.depth 
            self.colorMode = self.ds.PhotometricInterpretation
            self.PatientName.setText(f"{self.ds.get('PatientName','Missing')}")
            self.PatientAge.setText(f"{self.ds.get('PatientAge','Missing')}")
            self.Modality.setText(f"{self.ds.get('Modality','Missing')}")
            self.BodyPart.setText(f"{self.ds.get('BodyPartExamined', 'Missing')}")
            self.ImageDim.setText(f"{self.height,self.width}")
            self.ImageColor.setText(f"{self.colorMode}")
            self.ImageSize.setText(f"{self.size}")
            self.BitDepth.setText(f"{self.depth}")
            plt.imshow(self.ds.pixel_array)
            plt.axis('off')
            self.canvas_1.draw()
        except Exception as e: 
            self.displayError(e)
            print(e) 
    
    def convertToGrayScaleAndScale(self,interpolate=False):
        if not self.path: 
            self.displayError('Select an image')
            return
        self.scaleFactor = float(self.ScaleEdit.text())
        if self.suffix=='dcm': self.grayScaledImg = Image.fromarray(self.ds.pixel_array).convert('L')
        else: self.grayScaledImg = self.image.convert('L')
        self.grayScaledImgArr = np.array(self.grayScaledImg)
        if interpolate==True:
            self.initialW = self.grayScaledImg.size[0]
            self.initialH = self.grayScaledImg.size[1]
            self.newW = math.ceil(self.initialW * self.scaleFactor)
            self.newH = math.ceil(self.initialH * self.scaleFactor)
            self.newImgArrNearestN=np.zeros((self.newW,self.newH)) 
            self.newImgArrBilinear=np.zeros((self.newW,self.newH))
            if (not self.grayScaledImg): self.displayError('Please select a photo')
            else: self.interpolate()

    def displayGrayScaledImg(self):
        try:
            self.convertToGrayScaleAndScale()
            plt.clf()
            plt.draw()
            plt.imshow(self.grayScaledImgArr)
            self.canvas_1.draw()
        except: return

    def interpolate(self):
        try:
            for i in range(self.newW):
                for j in range(self.newH):
                    self.newImgArrNearestN[i][j] = self.grayScaledImgArr[math.floor(i/self.scaleFactor)][math.floor(j/self.scaleFactor)]
                    newRelativeXpos = i/self.newW
                    newRelativeYpos = j/self.newH
                    initialRelativeXposition = newRelativeXpos*self.initialW
                    initialRelativeYposition = newRelativeYpos*self.initialH
                    previousXposition = int(np.floor(initialRelativeXposition))
                    previousYposition = int(np.floor(initialRelativeYposition))
                    nextXposition = previousXposition+1
                    nextYposition = previousYposition+1
                    previousXposition = min(previousXposition,self.initialW-1)
                    previousYposition = min(previousYposition,self.initialH-1)
                    nextXposition = min(nextXposition,self.initialW-1)
                    nextYposition = min(nextYposition,self.initialH-1)
                    dxNext = nextXposition - initialRelativeXposition
                    dyNext = nextYposition - initialRelativeYposition
                    dxPrev = 1 - dxNext
                    dyPrev = 1 - dyNext
                    self.newImgArrBilinear[i][j] = dyPrev * (self.grayScaledImgArr[previousXposition][nextXposition] * dxNext + self.grayScaledImgArr[nextXposition][nextYposition] * dxPrev) \
                + dyNext * (self.grayScaledImgArr[previousXposition][previousYposition] * dxNext + self.grayScaledImgArr[nextXposition][previousYposition] * dxPrev)
            plt.figure(self.figureScale.number)
            plt.imshow(self.newImgArrBilinear, interpolation='None', cmap='gray')
            plt.draw()
            print('self.newImgArrBilinear')
        except Exception as e:
            print('return')

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