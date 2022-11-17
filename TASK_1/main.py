from PyQt5 import QtWidgets
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
        loadUi('UI.ui', self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_2.addWidget(self.canvas)
        self.actionBrowse.triggered.connect(self.openFileDialogue)

    def openFileDialogue(self,str="Load Image File"):
        self.path,_ = QtWidgets.QFileDialog.getOpenFileName()
        suffix = self.path.split('.')[-1]
        if suffix=='dcm': self.openDicom()
        else: self.openImage()

    def openImage(self):
        try: image = Image.open(self.path)
        except Exception as e: self.displayError(e) 
        image = Image.open(self.path)
        self.width = image.width
        self.height = image.height
        try: self.depth = math.ceil(math.log(np.amax(image) - np.amin(image) + 1, 2)) * np.shape(image)[2]
        except: self.depth = math.ceil(math.log(np.amax(image) - np.amin(image) + 1, 2))
        self.size = self.width * self.height * self.depth
        self.colorMode = image.mode
        self.ImageDim.setText(f"{self.height,self.width}")
        self.ImageColor.setText(f"{self.colorMode}")
        self.ImageSize.setText(f"{self.size}")
        self.BitDepth.setText(f"{self.depth}")
        self.PatientName.setText("None")
        self.PatientAge.setText("None")
        self.Modality.setText("None")
        self.BodyPart.setText("None")
        plt.imshow(image)
        plt.axis('off')
        self.canvas.draw()

        
    
    def openDicom(self):
        try:
            ds = dicom.dcmread(self.path)
            self.width =  ds.Columns 
            self.height =  ds.Rows 
            self.depth =  ds.BitsAllocated
            self.size = self.width * self.height * self.depth 
            self.colorMode = ds.PhotometricInterpretation
            self.PatientName.setText(f"{ds.get('PatientName','Missing')}")
            self.PatientAge.setText(f"{ds.get('PatientAge','Missing')}")
            self.Modality.setText(f"{ds.get('Modality','Missing')}")
            self.BodyPart.setText(f"{ds.get('BodyPartExamined', 'Missing')}")
            self.ImageDim.setText(f"{self.height,self.width}")
            self.ImageColor.setText(f"{self.colorMode}")
            self.ImageSize.setText(f"{self.size}")
            self.BitDepth.setText(f"{self.depth}")
            plt.imshow(ds.pixel_array)
            plt.axis('off')
            self.canvas.draw()
        except Exception as e: self.displayError(e) 

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