from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import os
from PIL import Image

class EasyEditor(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.Image = None
        self.save_folder = "Edited/"
        self.connects()

    def connects(self):
        self.ui.open_file.triggered.connect(self.choose_folder)
        self.ui.list.currentRowChanged.connect(self.show_chosen_image)
        
    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            pass

    def load_image(self, filename):
        self.filename = os.path.join(self.workdir, filename)
        self.image = Image.open(self.filename)

    def show_image(self):
        self.ui.picture.hide()
        h = self.ui.picture.height()
        w = self.ui.picture.width()

        pm_image = QPixmap(self.filename)
        pm_image = pm_image.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.picture.setPixmap(pm_image)
        self.ui.picture.show()
        

    def show_image_list(self):
        filenames = os.listdir(self.workdir)
        self.ui.list.clear()
        images = self.filter(filenames)
        self.ui.list.addItems(images)   

    def filter(self, filenames):
        images = []
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith('.jpeg') or filename.endswith('.png'):
                images.append(filename)

            return images

    def show_chosen_image(self):
        if self.ui.list.currentRow() >= 0:
            filename = self.ui.list.currentItem().text()
            self.load_image(filename)
            self.show_image()

app = QApplication([])
ex = EasyEditor()
ex.show()
app.exec_()