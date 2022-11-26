from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PIL import Image
import numpy as np
import sys

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('interface.ui', self)
        self.imageArr = []

    def displayError(self,e):
        error = QMessageBox()
        error.setIcon(QMessageBox.Critical)
        error.setWindowTitle('Error')
        error.setText('Error')
        error.setInformativeText(f"{e}")
        error.exec_()
        return
    
    def openFileDialogue(self):
        try:
            self.path,_ = QFileDialog.getOpenFileName()
            self.suffix = self.path.split('.')[-1]
            self.image = Image.open(self.path)
            self.imageArr = np.array(self.image)
        except Exception as e: self.displayError(e)


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())