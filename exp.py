from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap

from ui import Ui_MainWindow
import os

from PIL import Image, ImageFilter, ImageOps

def connects(self):
    self.inTheRight.triggered.connect(self.do_left)
    self.inTheLeft.triggered.connect(self.do_right)

def do_left(self):
    if self.image:
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.show_image()

def do_left(self):
    if self.image:
        self.image = self.image.mirror(self.image)
        self.save_image()
        self.show_image()

def do_gblur(self):
    if self.image:
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=10))
        self.save_image()
        self.show_image()

def do_bblur(self):
    if self.image:
        self.image = self.image.filter(ImageFilter.BoxBlur(10)) 
        self.save_image()
        self.show_image()

def do_sharp(self):
    if self.image:
        self.image = self.image(ImageFilter.SHARPEN(10))