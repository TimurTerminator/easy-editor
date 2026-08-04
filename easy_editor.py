from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog
import os
from PIL import Image, ImageFilter
from PIL import ImageOps
from PyQt5.QtGui import QPixmap
from PIL.ImageFilter import SHARPEN
app = QApplication([])
main = QWidget()
main.resize(800, 600)
main.setWindowTitle('Easy Editor')

folder = QPushButton('Папка')
list_elements = QListWidget()
picture = QLabel('Картинка')

button_left = QPushButton('Лево')
button_right = QPushButton('Право')
button_flip = QPushButton('Зеркало')
button_sharpness = QPushButton('Резкость')
button_bw = QPushButton('Ч/Б')
button_mirror = QPushButton('Размыть')
button_save = QPushButton('Сохранить')
button_resetFilters = QPushButton('Сбросить фильтры')

v1 = QVBoxLayout()
v1.addWidget(folder, alignment = Qt.AlignCenter)
v1.addWidget(list_elements)

h2 = QHBoxLayout()
h2.addWidget(button_left)
h2.addWidget(button_right)
h2.addWidget(button_flip)
h2.addWidget(button_sharpness)
h2.addWidget(button_bw)
h2.addWidget(button_mirror)
h2.addWidget(button_save)
h2.addWidget(button_resetFilters)

v3 = QVBoxLayout()
v3.addWidget(picture)
v3.addLayout(h2)

g = QHBoxLayout()
g.addLayout(v1, 20)
g.addLayout(v3, 70)
main.setLayout(g)


workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result            

def showFilenameslist():
    extension = ['.png', '.jpg', '.gif', '.jpeg', '.tiff', '.raw', '.psd', '.pdf', '.eps', '.ai', '.cdr', '.svg']
    chooseWorkdir()
    photo = filter(os.listdir(workdir), extension)
    list_elements.clear()
    for file in photo:
        list_elements.addItem(file)
folder.clicked.connect(showFilenameslist)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.folder_name = 'workdir/'
        self.original_image = None
    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width, label_height = picture.width(), picture.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        picture.setPixmap(scaled_pixmap)
        picture.setVisible(True)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.folder_name, self.filename)
        self.showImage(image_path)
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(
            workdir, self.folder_name, self.filename
        )
        self.showImage(image_path)
    def do_sharpness(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder_name, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.rotate(-90)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder_name, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.rotate(90)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder_name, self.filename)
        self.showImage(image_path)
    def do_mirror(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder_name, self.filename)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join(workdir, self.folder_name)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def resetImage(self):
        self.image = self.original_image.copy()
        self.showImage(os.path.join(workdir, self.filename))
    
workimage = ImageProcessor()

def showChosenImage():
    if list_elements.currentRow() >= 0:
        filename = list_elements.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)
list_elements.currentRowChanged.connect(showChosenImage)
button_bw.clicked.connect(workimage.do_bw)
button_flip.clicked.connect(workimage.do_flip)
button_sharpness.clicked.connect(workimage.do_sharpness)
button_left.clicked.connect(workimage.do_left)
button_right.clicked.connect(workimage.do_right)
button_mirror.clicked.connect(workimage.do_mirror)
button_save.clicked.connect(workimage.saveImage)
button_resetFilters.clicked.connect(workimage.resetImage)
main.show()
app.exec_()
