
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from ui import Ui_MainWindow
import os

class EasyEditor(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.connects()

    def connects(self):
        self.ui.open_file.triggered.connect(self.choose_folder)
        
    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            pass
        
    def show_image_list(self):
        filenames = os.listdir(self.workdir)
        self.ui.list.clear()
        images = self.filter(filenames)
        self.ui.list.addItems(filenames)   

    def filter(self, filenames):
        images = []
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith('.jpeg') or filename.endswith('.png'):
                images.append(filename)

            return images


app = QApplication([])
ex = EasyEditor()
ex.show()
app.exec_()