import sys
from builtins import print

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFileDialog, QAction, QScrollArea, QVBoxLayout, QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgba
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt

class Ui_MainWindow(object):
    scale = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 756)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(500, 40, 121, 31))
        self.LoadButton.setObjectName("LoadButton")

        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(500, 90, 121, 31))
        self.SaveButton.setObjectName("SaveButton")

        self.ChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeButton.setGeometry(QtCore.QRect(250, 390, 121, 31))
        self.ChangeButton.setObjectName("ChangeButton")

        self.ResizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResizeButton.setGeometry(QtCore.QRect(250, 440, 121, 31))
        self.ResizeButton.setObjectName("ResizeButton")

        self.HistButton = QtWidgets.QPushButton(self.centralwidget)
        self.HistButton.setGeometry(QtCore.QRect(390, 390, 121, 31))
        self.HistButton.setObjectName("HistButton")

        self.BrightButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrightButton.setGeometry(QtCore.QRect(530, 390, 121, 31))
        self.BrightButton.setObjectName("BrightButton")

        self.DarkButton = QtWidgets.QPushButton(self.centralwidget)
        self.DarkButton.setGeometry(QtCore.QRect(530, 440, 121, 31))
        self.DarkButton.setObjectName("DarkButton")

        self.StretchButton = QtWidgets.QPushButton(self.centralwidget)
        self.StretchButton.setGeometry(QtCore.QRect(250, 490, 121, 31))
        self.StretchButton.setObjectName("StretchButton")

        self.EqualizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.EqualizeButton.setGeometry(QtCore.QRect(390, 440, 121, 31))
        self.EqualizeButton.setObjectName("EqualizeButton")

        self.ManualThresholdButton = QtWidgets.QPushButton(self.centralwidget)
        self.ManualThresholdButton.setGeometry(QtCore.QRect(250, 540, 121, 31))
        self.ManualThresholdButton.setObjectName("ManualThresholdButton")

        self.NiblackThresholdButton = QtWidgets.QPushButton(self.centralwidget)
        self.NiblackThresholdButton.setGeometry(QtCore.QRect(250, 590, 121, 31))
        self.NiblackThresholdButton.setObjectName("NiblackThresholdButton")

        self.ToGrayScaleButton = QtWidgets.QPushButton(self.centralwidget)
        self.ToGrayScaleButton.setGeometry(QtCore.QRect(390, 490, 121, 31))
        self.ToGrayScaleButton.setObjectName("ToGrayScaleButton")

        self.OtsuThresholdButton = QtWidgets.QPushButton(self.centralwidget)
        self.OtsuThresholdButton.setGeometry(QtCore.QRect(390, 540, 121, 31))
        self.OtsuThresholdButton.setObjectName("OtsuThresholdButton")

        self.CreateMaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.CreateMaskButton.setGeometry(QtCore.QRect(250, 640, 121, 31))
        self.CreateMaskButton.setObjectName("CreateMaskButton")

        self.ConvFilterButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConvFilterButton.setGeometry(QtCore.QRect(390, 640, 121, 31))
        self.ConvFilterButton.setObjectName("ConvFilterButton")
        self.ConvFilterButton.setEnabled(False)

        self.KuwaharaButton = QtWidgets.QPushButton(self.centralwidget)
        self.KuwaharaButton.setGeometry(QtCore.QRect(250, 690, 121, 31))
        self.KuwaharaButton.setObjectName("KuwaharaButton")

        self.MedianButton = QtWidgets.QPushButton(self.centralwidget)
        self.MedianButton.setGeometry(QtCore.QRect(390, 690, 121, 31))
        self.MedianButton.setObjectName("MedianButton")

        self.MaskSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaskSizeLabel.setGeometry(QtCore.QRect(156, 620, 47, 13))
        self.MaskSizeLabel.setText("Mask Size")
        self.MaskSizeLabel.setObjectName("MaskSizeLabel")

        self.MaskSizeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.MaskSizeComboBox.setGeometry(QtCore.QRect(156, 640, 75, 21))
        self.MaskSizeComboBox.setObjectName("MaskSizeComboBox")
        self.MaskSizeComboBox.addItems(["3x3","5x5"])

        self.WindowSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.WindowSizeLabel.setGeometry(QtCore.QRect(156, 670, 75, 13))
        self.WindowSizeLabel.setText("Window Size")
        self.WindowSizeLabel.setObjectName("WindowSizeLabel")

        self.WindowSizeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.WindowSizeComboBox.setGeometry(QtCore.QRect(156, 690, 75, 21))
        self.WindowSizeComboBox.setObjectName("WindowSizeComboBox")
        self.WindowSizeComboBox.addItems(["3", "5"])

        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 441, 321))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignTop)

        self.RLabel = QtWidgets.QLabel(self.centralwidget)
        self.RLabel.setGeometry(QtCore.QRect(40, 370, 47, 13))
        self.RLabel.setText("R")
        self.RLabel.setObjectName("RLabel")

        self.GLabel = QtWidgets.QLabel(self.centralwidget)
        self.GLabel.setGeometry(QtCore.QRect(110, 370, 47, 13))
        self.GLabel.setText("G")
        self.GLabel.setObjectName("GLabel")

        self.BLabel = QtWidgets.QLabel(self.centralwidget)
        self.BLabel.setGeometry(QtCore.QRect(180, 370, 47, 13))
        self.BLabel.setText("B")
        self.BLabel.setObjectName("BLabel")

        self.ScaleLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScaleLabel.setGeometry(QtCore.QRect(180, 420, 47, 13))
        self.ScaleLabel.setText("Scale")
        self.ScaleLabel.setObjectName("ScaleLabel")

        self.ThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.ThresholdLabel.setGeometry(QtCore.QRect(180, 520, 47, 13))
        self.ThresholdLabel.setText("Threshold")
        self.ThresholdLabel.setObjectName("ThresholdLabel")

        self.RtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.RtextEdit.setGeometry(QtCore.QRect(40, 390, 51, 21))
        self.RtextEdit.setObjectName("RtextEdit")
        self.RtextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RtextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.GtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.GtextEdit.setGeometry(QtCore.QRect(110, 390, 51, 21))
        self.GtextEdit.setObjectName("GtextEdit")
        self.GtextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GtextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.BtextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.BtextEdit.setGeometry(QtCore.QRect(180, 390, 51, 21))
        self.BtextEdit.setObjectName("BtextEdit")
        self.BtextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.BtextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.ScaleTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ScaleTextEdit.setGeometry(QtCore.QRect(180, 440, 51, 21))
        self.ScaleTextEdit.setObjectName("ScaleTextEdit")
        self.ScaleTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ScaleTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.ThresholdTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ThresholdTextEdit.setGeometry(QtCore.QRect(180, 540, 51, 21))
        self.ThresholdTextEdit.setObjectName("ThresholdTextEdit")
        self.ThresholdTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ThresholdTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.ABrightnessTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ABrightnessTextEdit.setGeometry(QtCore.QRect(30, 490, 94, 21))
        self.ABrightnessTextEdit.setObjectName("ABrightnessTextEdit")
        self.ABrightnessTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ABrightnessTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.BBrightnessTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.BBrightnessTextEdit.setGeometry(QtCore.QRect(137, 490, 94, 21))
        self.BBrightnessTextEdit.setObjectName("BBrightnessTextEdit")
        self.BBrightnessTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.BBrightnessTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.ABrightnessLabel = QtWidgets.QLabel(self.centralwidget)
        self.ABrightnessLabel.setGeometry(QtCore.QRect(30, 470, 94, 13))
        self.ABrightnessLabel.setText("A Brightness Range")
        self.ABrightnessLabel.setObjectName("ABrightnessLabel")

        self.BBrightnessLabel = QtWidgets.QLabel(self.centralwidget)
        self.BBrightnessLabel.setGeometry(QtCore.QRect(137, 470, 94, 13))
        self.BBrightnessLabel.setText("B Brightness Range")
        self.BBrightnessLabel.setObjectName("BBrightnessLabel")

        self.WidnowSizeTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.WidnowSizeTextEdit.setGeometry(QtCore.QRect(30, 590, 94, 21))
        self.WidnowSizeTextEdit.setObjectName("WidnowSizeTextEdit")
        self.WidnowSizeTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.WidnowSizeTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.KParameterTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.KParameterTextEdit.setGeometry(QtCore.QRect(137, 590, 94, 21))
        self.KParameterTextEdit.setObjectName("KParameterTextEdit")
        self.KParameterTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.KParameterTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.WindowSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.WindowSizeLabel.setGeometry(QtCore.QRect(30, 570, 94, 13))
        self.WindowSizeLabel.setText("Window Size (odd)")
        self.WindowSizeLabel.setObjectName("WindowSizeLabel")

        self.KParameterLabel = QtWidgets.QLabel(self.centralwidget)
        self.KParameterLabel.setGeometry(QtCore.QRect(137, 570, 94, 13))
        self.KParameterLabel.setText("Parameter K")
        self.KParameterLabel.setObjectName("KParameterLabel")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.LoadButton.clicked.connect(self.openImage)
        self.SaveButton.clicked.connect(self.saveImage)
        self.ChangeButton.clicked.connect(self.changePixel)
        self.ResizeButton.clicked.connect(self.resizeImage)
        self.HistButton.clicked.connect(self.calcHist)
        self.BrightButton.clicked.connect(self.brightImage)
        self.DarkButton.clicked.connect(self.darkImage)
        self.StretchButton.clicked.connect(self.stretchHist)
        self.EqualizeButton.clicked.connect(self.equalizeHistogram)
        self.ManualThresholdButton.clicked.connect(self.manualThreshold)
        self.ToGrayScaleButton.clicked.connect(self.toGrayScale)
        self.OtsuThresholdButton.clicked.connect(self.otsuThresholding)
        self.NiblackThresholdButton.clicked.connect(self.niblackThresholding)
        self.CreateMaskButton.clicked.connect(self.createMask)
        self.ConvFilterButton.clicked.connect(self.convFilter)
        self.KuwaharaButton.clicked.connect(self.kuwaharaFilter)
        self.MedianButton.clicked.connect(self.medianFilter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadButton.setText(_translate("MainWindow", "Load Graphic File"))
        self.SaveButton.setText(_translate("MainWindow", "Save Graphic File"))
        self.ChangeButton.setText(_translate("MainWindow", "Change Pixel"))
        self.ResizeButton.setText(_translate("MainWindow", "Show Bigger Image"))
        self.HistButton.setText(_translate("MainWindow", "Calculate Histogram"))
        self.BrightButton.setText(_translate("MainWindow", "Brighten Image"))
        self.DarkButton.setText(_translate("MainWindow", "Darken Image"))
        self.StretchButton.setText(_translate("MainWindow", "Stretch Histogram"))
        self.EqualizeButton.setText(_translate("MainWindow", "Equalize Histogram"))
        self.ManualThresholdButton.setText(_translate("MainWindow", "Manual Thresholding"))
        self.ToGrayScaleButton.setText(_translate("MainWindow", "Change to gray scale"))
        self.OtsuThresholdButton.setText(_translate("MainWindow", "Otsu Thresholding"))
        self.NiblackThresholdButton.setText(_translate("MainWindow", "Niblack Thresholding"))
        self.CreateMaskButton.setText(_translate("MainWindow", "Create Mask"))
        self.ConvFilterButton.setText(_translate("MainWindow", "Filter the Image"))
        self.KuwaharaButton.setText(_translate("MainWindow", "Kuwahara Filter"))
        self.MedianButton.setText(_translate("MainWindow", "Median Filter"))


    def openImage(self):
        global img
        global pixmap
        global pixmap_scaled

        self.imagePath, _ = QFileDialog.getOpenFileName()
        print('filepath: ', self.imagePath)
        img = QImage(self.imagePath)
        pixmap = QPixmap(QPixmap.fromImage(img))
        pixmap_scaled = pixmap.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
        img = pixmap_scaled.toImage()

        self.imageLabel.setPixmap(pixmap_scaled)
        self.imageLabel.mousePressEvent = self.getPixel

    def saveImage(self):
        if (self.imageLabel.pixmap() is not None):

            path = QFileDialog.getSaveFileName(None, "choose save file name", "./image.png", "PNG (*.png);;JPEG (*.jpeg);;JPG (*.jpg);;GIF (*.gif);;BMP (*.bmp);;TIFF (*.tiff)")  # PyQt5 nie wspiera zapisywania formatu GIF (.gif), dlatego można odczytać ale nie zapisać
            pix = self.imageLabel.pixmap()
            img = QImage(QPixmap.toImage(pix))
            img.save(path[0])
        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()

    def getPixel(self, event):
        global x
        global y
        global isBigger

        isBigger = False

        x = event.pos().x()
        y = event.pos().y()

        pixmap_tmp = self.imageLabel.pixmap()

        c = pixmap_tmp.toImage().pixel(x, y)
        rgb = QColor(c).getRgb()

        self.RtextEdit.setPlainText(str(rgb[0]))
        self.GtextEdit.setPlainText(str(rgb[1]))
        self.BtextEdit.setPlainText(str(rgb[2]))

    def changePixel(self):
        global img_copy
        if (self.imageLabel.pixmap() is not None and self.RtextEdit.toPlainText() and self.GtextEdit.toPlainText() and self.BtextEdit.toPlainText() and ( x != -1 or bigger_x != -1) and (y != -1 or bigger_y != -1)):
            r = int(self.RtextEdit.toPlainText())
            g = int(self.GtextEdit.toPlainText())
            b = int(self.BtextEdit.toPlainText())

            pixmap_tmp = self.imageLabel.pixmap()
            img_tmp = QImage(QPixmap.toImage(pixmap_tmp))
            img_copy = img_tmp.copy()
            if (isBigger):
                img_copy.setPixel(int(bigger_x / self.scale), int(bigger_y / self.scale), QColor(r, g, b, 255).rgb())
                img_tmp.setPixel(int(bigger_x / self.scale), int(bigger_y / self.scale), QColor(r, g, b, 255).rgb())
            else:
                img_copy.setPixel(x, y, QColor(r, g, b, 255).rgb())
                img_tmp.setPixel(x, y, QColor(r, g, b, 255).rgb())

            tmp_pixamp = QPixmap(QPixmap.fromImage(img_copy))
            self.imageLabel.setPixmap(tmp_pixamp)

            img_before = img_tmp.copy()
            img_after = img_before.scaled(img.width() * self.scale, img.height() * self.scale, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

            if (isSecondWindow):
                if (isBigger):
                    img_after.setPixel(bigger_x, bigger_y, QColor(r, g, b, 255).rgb())
                    tmp_pixamp2 = QPixmap(QPixmap.fromImage(img_after))
                    self.w.label.setPixmap(tmp_pixamp2)
                else:
                    img_after.setPixel(int(x * self.scale), int(y * self.scale), QColor(r, g, b, 255).rgb())
                    tmp_pixamp2 = QPixmap(QPixmap.fromImage(img_after))
                    self.w.label.setPixmap(tmp_pixamp2)

        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded\n- You didn't pick any pixel by clicking on the image\n- The text fields for RGB are empty ")
            msg.exec()

    def createMessageBox(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        return msgBox

    def resizeImage(self):
        global img
        global img_after

        if (self.imageLabel.pixmap() is not None and self.ScaleTextEdit.toPlainText()):
            img_after = QImage()

            self.scale = int(self.ScaleTextEdit.toPlainText())

            pixmap_tmp = self.imageLabel.pixmap()
            img_tmp = QImage(QPixmap.toImage(pixmap_tmp))
            img_before = img_tmp.copy()
            img_after = img_before.scaled(img.width() * self.scale, img.height() * self.scale, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

            if (isSecondWindow):
                self.w.close()
                self.w = Window2()
                self.w.show()
            else:
                self.w = Window2()
                self.w.show()
        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded\n- The text field for Scale is empty ")
            msg.exec()

    def isGray(self):
        imagePIL = Image.open(self.imagePath).convert('RGB')

        w,h = imagePIL.size
        print(w,h)

        for i in range(w):
            for j in range(h):
                r,g,b = imagePIL.getpixel((i, j))
                if r != g != b: return False
        return True


    def calcHist(self):
        if (self.imageLabel.pixmap() is not None):
            imagePIL = Image.open(self.imagePath).convert('RGB')

            w,h = imagePIL.size
            print('width:', w)
            print('height', h)

            isgray = self.isGray()
            print(isgray)

            if(isgray):
                value = []

                for i in range(w):
                    for j in range(h):
                        c = imagePIL.getpixel((i, j))
                        value.append(c[0])

                plt.hist(value,256,[0,256])
                plt.savefig('hist-gray.jpg')
                plt.show()
            else:
                value_r = []
                value_g = []
                value_b = []

                for i in range(w):
                    for j in range(h):
                        r, g, b = imagePIL.getpixel((i, j))
                        value_r.append(r)
                        value_g.append(g)
                        value_b.append(b)

                value_avg = []

                for x in range(len(value_r)):
                    if(value_r[x] + value_g[x] + value_b[x] == 0):
                        value_avg.append(0)
                    else:
                        value_avg.append((value_r[x] + value_g[x] + value_b[x])/3)

                fig, axes = plt.subplots(nrows=2, ncols=2)
                ax0, ax1, ax2, ax3 = axes.flatten()
                ax0.hist(value_r, 256, [0, 256], color = "red")
                ax0.set_title('Kanał R')
                ax1.hist(value_g, 256, [0, 256], color = "green")
                ax1.set_title('Kanał G')
                ax2.hist(value_b, 256, [0, 256], color = "blue")
                ax2.set_title('Kanał B')
                ax3.hist(value_avg, 256, [0, 256], color = "black")
                ax3.set_title('Dla wartości uśrednionych')

                fig.tight_layout()
                plt.savefig('hist.jpg')
                plt.show()

        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()


    def brightImage(self):
        if (self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            c = int(255 / np.log(255 + 1))

            brightened_image = Image.new('RGB', image_original.size)
            brightened_image_data = []

            for pixel in pixels:
                new_pixel = (int(c * np.log(pixel[0] + 1)), int(c * np.log(pixel[1] + 1)), int(c * np.log(pixel[2] + 1)))

                brightened_image_data.append(new_pixel)

            brightened_image.putdata(brightened_image_data)
            brightened_image.save('bright.jpg')

            img = ImageQt(brightened_image)

            pixmap = QPixmap(QPixmap.fromImage(img))
            pixmap_scaled = pixmap.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_scaled)
        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()


    def darkImage(self):
        if (self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            #c = int(255 / np.log(255 + 1))
            c = 255
            n = 2.5

            darkened_image = Image.new('RGB', image_original.size)
            darkened_image_data = []

            for pixel in pixels:
                new_pixel = (int(c * np.power(pixel[0]/255,n)), int(c * np.power(pixel[1]/255,n)), int(c * np.power(pixel[2]/255,n)))

                darkened_image_data.append(new_pixel)

            darkened_image.putdata(darkened_image_data)
            darkened_image.save('dark.jpg')

            img = ImageQt(darkened_image)

            pixmap = QPixmap(QPixmap.fromImage(img))
            pixmap_scaled = pixmap.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_scaled)
        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()

    def stretchHist(self):
        if (self.imageLabel.pixmap() is not None and self.ABrightnessTextEdit.toPlainText() and self.BBrightnessTextEdit.toPlainText()):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            stretched_image = Image.new('RGB', image_original.size)
            stretched_image_data = []

            isgray = self.isGray()
            if (isgray):

                value = []

                for pixel in pixels:
                    value.append(pixel[0])

                stretched = self.stretchFunction(value)

                for pixel in stretched:
                    stretched_image_data.append((pixel,pixel,pixel))

                stretched_image.putdata(stretched_image_data)
                stretched_image.save('strechrtedImage - gray.jpg')
                img = ImageQt(stretched_image)

                pixmap_stretched = QPixmap(QPixmap.fromImage(img))
                pixmap_stretched = pixmap_stretched.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
                self.imageLabel.setPixmap(pixmap_stretched)

                stretched4Hist = []

                for i in range(len(stretched)):
                    if(stretched[i] != 0 and stretched[i] != 255):
                        stretched4Hist.append(stretched[i])

                plt.hist(stretched4Hist, 256, [0, 256])
                plt.savefig('stretch-gray.jpg')
                plt.show()

            else:
                value_r = []
                value_g = []
                value_b = []

                for pixel in pixels:
                    value_r.append(pixel[0])
                    value_g.append(pixel[1])
                    value_b.append(pixel[2])

                stretched_r = self.stretchFunction(value_r)
                stretched_g = self.stretchFunction(value_g)
                stretched_b = self.stretchFunction(value_b)

                for i in range(len(stretched_r)):
                    stretched_image_data.append((stretched_r[i], stretched_g[i], stretched_b[i]))

                stretched_image.putdata(stretched_image_data)
                stretched_image.save('strechtedImage.jpg')
                img = ImageQt(stretched_image)

                pixmap_stretched = QPixmap(QPixmap.fromImage(img))
                pixmap_stretched = pixmap_stretched.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
                self.imageLabel.setPixmap(pixmap_stretched)

                stretched4Hist_r = []
                stretched4Hist_g = []
                stretched4Hist_b = []

                for i in range(len(stretched_r)):
                    if (stretched_r[i] != 0 and stretched_r[i] != 255):
                        stretched4Hist_r.append(stretched_r[i])
                    if (stretched_g[i] != 0 and stretched_g[i] != 255):
                        stretched4Hist_g.append(stretched_g[i])
                    if (stretched_b[i] != 0 and stretched_b[i] != 255):
                        stretched4Hist_b.append(stretched_b[i])

                fig, axes = plt.subplots(nrows=2, ncols=2)
                ax0, ax1, ax2, ax3 = axes.flatten()
                ax0.hist(stretched4Hist_r, 256, [0, 256], color="red")
                ax0.set_title('Kanał R')
                ax1.hist(stretched4Hist_g, 256, [0, 256], color="green")
                ax1.set_title('Kanał G')
                ax2.hist(stretched4Hist_b, 256, [0, 256], color="blue")
                ax2.set_title('Kanał B')

                fig.tight_layout()
                plt.savefig('stretch.jpg')
                plt.show()
        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded\n- The text fields for brightness range are empty ")
            msg.exec()

    def stretchFunction(self, values):
        a = int(self.ABrightnessTextEdit.toPlainText())
        b = int(self.BBrightnessTextEdit.toPlainText())

        stretched_values = []
        for i in range(len(values)):
            if(values[i] < a):
                stretched_values.append(0)
            elif(values[i] > b):
                stretched_values.append(255)
            else:
                stretched_values.append(int((values[i] - a) / (b - a) * 255))

        return stretched_values


    def equalizeHistogram(self):
        if (self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            image_equalized = Image.new('RGB', image_original.size)
            image_equalized_data = []

            pixelsAmount = len(pixels)
            print('Liczba pikseli na obrazie: ', pixelsAmount)
            isgray = self.isGray()
            if(isgray):

                values = []

                for pixel in pixels:
                    values.append(pixel[0])
                counted_values = self.pixelCounter(values)

                distribution = self.calculateDistribution(counted_values,pixelsAmount)
                LUT_table = self.calculateLUTTable(distribution)

                for value in values:
                    image_equalized_data.append((LUT_table[value], LUT_table[value], LUT_table[value]))

                image_equalized.putdata(image_equalized_data)
                image_equalized.save('equalizedImage-gray.jpg')
                img = ImageQt(image_equalized)

                pixmap_equalized = QPixmap(QPixmap.fromImage(img))
                pixmap_equalized = pixmap_equalized.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
                self.imageLabel.setPixmap(pixmap_equalized)

                equalized4Hist = []

                for i in range(len(values)):
                    equalized4Hist.append(LUT_table[values[i]])

                plt.hist(equalized4Hist, 256, [0, 256])
                plt.savefig('equalize-gray.jpg')
                plt.show()

            else:

                values_r = []
                values_g = []
                values_b = []

                for pixel in pixels:
                    values_r.append(pixel[0])
                    values_g.append(pixel[1])
                    values_b.append(pixel[2])

                counted_values_r = self.pixelCounter(values_r)
                counted_values_g = self.pixelCounter(values_g)
                counted_values_b = self.pixelCounter(values_b)

                distribution_r = self.calculateDistribution(counted_values_r, pixelsAmount)
                distribution_g = self.calculateDistribution(counted_values_g, pixelsAmount)
                distribution_b = self.calculateDistribution(counted_values_b, pixelsAmount)

                LUT_table_r = self.calculateLUTTable(distribution_r)
                LUT_table_g = self.calculateLUTTable(distribution_g)
                LUT_table_b = self.calculateLUTTable(distribution_b)

                for i in range(len(values_r)):
                    image_equalized_data.append((LUT_table_r[values_r[i]], LUT_table_g[values_g[i]], LUT_table_b[values_b[i]]))

                image_equalized.putdata(image_equalized_data)
                image_equalized.save('equalizedImage.jpg')
                img = ImageQt(image_equalized)

                pixmap_equalized = QPixmap(QPixmap.fromImage(img))
                pixmap_equalized = pixmap_equalized.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
                self.imageLabel.setPixmap(pixmap_equalized)

                equalized4Hist_r = []
                equalized4Hist_g = []
                equalized4Hist_b = []

                for i in range(len(values_r)):
                    equalized4Hist_r.append(LUT_table_r[values_r[i]])
                    equalized4Hist_g.append(LUT_table_g[values_g[i]])
                    equalized4Hist_b.append(LUT_table_b[values_b[i]])

                fig, axes = plt.subplots(nrows=2, ncols=2)
                ax0, ax1, ax2, ax3 = axes.flatten()
                ax0.hist(equalized4Hist_r, 256, [0, 256], color="red")
                ax0.set_title('Kanał R')
                ax1.hist(equalized4Hist_g, 256, [0, 256], color="green")
                ax1.set_title('Kanał G')
                ax2.hist(equalized4Hist_b, 256, [0, 256], color="blue")
                ax2.set_title('Kanał B')

                fig.tight_layout()
                plt.savefig('equalize.jpg')
                plt.show()
        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()


    def calculateLUTTable(self,distribution):
        LUT_table = []
        m = 256

        for i in range(len(distribution)):
            LUT_table.append(int(((distribution[i] - distribution[0]) / (1 - distribution[0])) * (m - 1)))

        return LUT_table

    def pixelCounter(self, values):

        counted_values = [0] * 256
        for value in values:
            counted_values[value] += 1;
        return counted_values

    def calculateDistribution(self,values, pixelsAmount):

        distribution = []
        dist = 0
        for i in range(len(values)):
            dist += values[i]/pixelsAmount
            distribution.append(dist)

        return distribution


    def manualThreshold(self):
        if (self.imageLabel.pixmap() is not None and self.ThresholdTextEdit.toPlainText()):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            image_after_thresholding = Image.new('RGB', image_original.size)
            image_after_thresholding_data = []

            threshold = int(self.ThresholdTextEdit.toPlainText())
            print('Próg: ', threshold)

            isgray = self.isGray()
            if(isgray == False):
                grayScaledPixels = self.toGrayScaleFunction(pixels)
            else:
                grayScaledPixels = pixels

            for pixel in grayScaledPixels:
                if(pixel[0] < threshold):
                    image_after_thresholding_data.append((0,0,0))
                elif(pixel[0] >= threshold):
                    image_after_thresholding_data.append((255,255,255))

            image_after_thresholding.putdata(image_after_thresholding_data)
            image_after_thresholding.save('manual_thresholding_result.jpg')

            img = ImageQt(image_after_thresholding)

            pixmap_thresholded = QPixmap(QPixmap.fromImage(img))
            pixmap_thresholded = pixmap_thresholded.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_thresholded)
            print('Koniec')


        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded\n- The text field for threshold is empty ")
            msg.exec()


    def toGrayScaleFunction(self,pixels):
        grayScaledPixels = []
        for pixel in pixels:
            grayScaledPixels.append((pixel[0], pixel[0], pixel[0]))

        return grayScaledPixels

    def toGrayScale(self):
        if(self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            grayScaledPixels = []
            for pixel in pixels:
                grayScaledPixels.append((pixel[0],pixel[0],pixel[0]))

            grayImage = Image.new('RGB', image_original.size)
            grayImage.putdata(grayScaledPixels)
            grayImage.save('RED.jpg')

            img = ImageQt(grayImage)

            pixmap_gray = QPixmap(QPixmap.fromImage(img))
            pixmap_gray = pixmap_gray.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_gray)
        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()

    def otsuThresholding(self):
        if (self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            pixels = image_original.getdata()

            image_after_otsu = Image.new('RGB', image_original.size)
            image_after_otsu_data = []

            pixel_amount = len(pixels)

            isgray = self.isGray()
            if (isgray == False):
                pixels = self.toGrayScaleFunction(pixels)

            one_channel_pixels = []
            for pixel in pixels:
                one_channel_pixels.append(pixel[0])

            counted_pixels = self.pixelCounter(one_channel_pixels)

            p_ob = 0
            p_b = 0
            mean_ob = 0
            mean_b = 0
            max_value = -1
            max_t = -1

            index_array = np.arange(256)

            probability_array = np.divide(counted_pixels,pixel_amount)

            for t in range(0,255):

                p_ob = np.sum(probability_array[:t])
                p_b = np.sum(probability_array[t:])

                if(p_ob == 0 or p_b == 0): continue

                mean_ob = np.sum(index_array[:t] * probability_array[:t]) / p_ob
                mean_b = np.sum(index_array[t:] * probability_array[t:]) / p_b

                value = p_ob * p_b * np.power(mean_ob - mean_b, 2)

                if(value > max_value):
                    max_value = value
                    max_t = t

            print('calculated threshold: ', max_t)
            for pixel in pixels:
                if (pixel[0] < max_t):
                    image_after_otsu_data.append((0, 0, 0))
                elif (pixel[0] >= max_t):
                    image_after_otsu_data.append((255, 255, 255))

            image_after_otsu.putdata(image_after_otsu_data)

            image_after_otsu.save('otsu_result.jpg')
            img = ImageQt(image_after_otsu)


            pixmap_otsu = QPixmap(QPixmap.fromImage(img))
            pixmap_otsu = pixmap_otsu.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_otsu)
            print('Koniec')
        else:
            msg = self.createMessageBox()
            msg.setText("There is no image loaded")
            msg.exec()


    def niblackThresholding(self):
        if (self.imageLabel.pixmap() is not None and self.KParameterTextEdit.toPlainText() and self.WidnowSizeTextEdit.toPlainText()):

            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            w,h = image_original.size

            isgray = self.isGray()
            if (isgray == False):
                for i in range(w):
                    for j in range(h):
                        pixel = image_original.getpixel((i,j))
                        image_original.putpixel((i,j),(pixel[0],pixel[0],pixel[0]))

            windowSize = int(self.WidnowSizeTextEdit.toPlainText())
            k = float(self.KParameterTextEdit.toPlainText())
            cellsInWindow = np.power(windowSize,2)

            image_copy = image_original.copy()

            windowRange = int(windowSize/2)

            z = 0                       #zmienna z jest tylko i wyłącznie w celu pokazania, iż algorytm pracuje
            for i in range(w):
                for j in range(h):

                    sum = 0
                    sum4var = 0

                    for x in range(-1 * windowRange, windowRange + 1):
                       for y in range(-1 * windowRange, windowRange + 1):
                            z += 1
                            if(i + x >= 0 and i + x < w and j + y >= 0 and j + y < h):
                                pixel_value = image_original.getpixel((i + x, j + y))
                                sum += pixel_value[0]
                            else:
                                sum += 0

                    avg = sum / cellsInWindow

                    for x in range(-1 * windowRange, windowRange + 1):
                        for y in range(-1 * windowRange, windowRange + 1):
                            z += 1
                            if(i + x >= 0 and i + x < w and j + y >= 0 and j + y < h):
                                pixel_value = image_original.getpixel((i + x, j + y))
                                sum4var += np.power(pixel_value[0] - avg, 2)
                            else:
                                sum4var += np.power(0 - avg,2)

                    var = sum4var / cellsInWindow
                    std_deviation = np.sqrt(var)
                    t = avg + (k * std_deviation)

                    pix = image_original.getpixel((i,j))
                    if(pix[0] < t):
                        image_copy.putpixel((i,j), (0,0,0))
                    else:
                        image_copy.putpixel((i,j),(255,255,255))

                    z += 1
                    print(z)

            image_copy.save('niblack_result.jpg')
            img = ImageQt(image_copy)

            pixmap_niblack = QPixmap(QPixmap.fromImage(img))
            pixmap_niblack = pixmap_niblack.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_niblack)
            print('Koniec')

        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded\n- The text field for parameter is empty \n- The text field for size of the window is empty ")
            msg.exec()

    def createMask(self):
        idx = int(self.MaskSizeComboBox.currentIndex())
        if(idx == 0): self.maskSize = 3
        elif(idx == 1): self.maskSize = 5

        self.maskWindow = MaskWindow(self.maskSize)
        self.maskWindow.exec()
        self.mask = self.maskWindow.mask

    def convFilter(self):
        if(self.imageLabel.pixmap() is not None):
            print(self.mask)

            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            w, h = image_original.size

            image_copy = image_original.copy()

            self.maskRange = int(self.maskSize/2)

            self.sumInMask = 0
            for i in range(self.maskSize):
                for j in range(self.maskSize):
                    self.sumInMask += self.mask[i][j]

            if(self.sumInMask == 0): self.sumInMask = 1
            print(self.sumInMask)

            isgray = self.isGray()
            if(isgray):
                for i in range(w):
                    for j in range(h):

                        sum = 0
                        for x in range(-1 * self.maskRange, self.maskRange + 1):
                            for y in range(-1 * self.maskRange, self.maskRange + 1):
                                if(i + x >= 0 and i + x < w and j + y >= 0 and j + y < h):
                                    pix_value = image_original.getpixel((i + x, j + y))
                                    sum += pix_value[0] * int(self.mask[x + self.maskRange][y + self.maskRange])
                                else:
                                    sum += 0

                        value = int(sum / self.sumInMask)

                        if(value > 255): value = 255
                        elif(value < 0): value = 0

                        image_copy.putpixel((i, j),(int(value), int(value), int(value)))
            else:
                for i in range(w):
                    for j in range(h):

                        sum_r = 0
                        sum_g = 0
                        sum_b = 0

                        for x in range(-1 * self.maskRange, self.maskRange + 1):
                            for y in range(-1 * self.maskRange, self.maskRange + 1):
                                if (i + x >= 0 and i + x < w and j + y >= 0 and j + y < h):
                                    pix_value = image_original.getpixel((i + x, j + y))
                                    sum_r += pix_value[0] * int(self.mask[x + self.maskRange][y + self.maskRange])
                                    sum_g += pix_value[1] * int(self.mask[x + self.maskRange][y + self.maskRange])
                                    sum_b += pix_value[2] * int(self.mask[x + self.maskRange][y + self.maskRange])
                                else:
                                    sum_r += 0
                                    sum_g += 0
                                    sum_b += 0


                        r_value = int(sum_r / self.sumInMask)
                        g_value = int(sum_g / self.sumInMask)
                        b_value = int(sum_b / self.sumInMask)

                        if (r_value > 255): r_value = 255
                        elif (r_value < 0): r_value = 0

                        if (g_value > 255): g_value = 255
                        elif (g_value < 0): g_value = 0

                        if (b_value > 255): b_value = 255
                        elif (b_value < 0): b_value = 0

                        image_copy.putpixel((i, j), (int(r_value), int(g_value), int(b_value)))

            image_copy.save('convFilter_result.jpg')
            img = ImageQt(image_copy)

            pixmap_convFilter = QPixmap(QPixmap.fromImage(img))
            pixmap_convFilter = pixmap_convFilter.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_convFilter)
            print('Koniec')
        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded\n- There is no mask properly saved (you didn't click the save button in mask window) ")
            msg.exec()

    def kuwaharaFilter(self):
        if(self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            w, h = image_original.size

            image_copy = image_original.copy()

            idx = int(self.WindowSizeComboBox.currentIndex())
            if (idx == 0): size = 3
            elif (idx == 1): size = 5

            self.maskRange = int(size / 2)
            self.cellsInSubWindow = np.power(self.maskRange + 1, 2)

            isgray = self.isGray()
            if(isgray):
                z = 0
                for i in range(w):
                    for j in range(h):

                        mean = np.zeros(4)

                        var = np.zeros(4)

                        for x in range(self.maskRange + 1):
                            for y in range(self.maskRange + 1):
                                z += 1
                                if (x - self.maskRange + i >= 0 and y - self.maskRange + j >= 0):
                                    mean[0] += image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[0] / self.cellsInSubWindow

                                if (x + i >= 0 and x + i < w and y - self.maskRange + j >= 0 and y - self.maskRange + j < h):
                                    mean[1] += image_original.getpixel((x + i, y - self.maskRange + j))[0] / self.cellsInSubWindow

                                if (x - self.maskRange + i >= 0 and x - self.maskRange + i < w and y + j >= 0 and y + j < h):
                                    mean[2] += image_original.getpixel((x - self.maskRange + i, y + j))[0] / self.cellsInSubWindow

                                if (x + i < w and y + j < h):
                                    mean[3] += image_original.getpixel((x + i, y + j))[0] / self.cellsInSubWindow

                        for x in range(self.maskRange + 1):
                            for y in range(self.maskRange + 1):
                                z += 1
                                if (x - self.maskRange + i >= 0 and y - self.maskRange + j >= 0):
                                    var[0] += np.power(image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[0] - mean[0], 2) / self.cellsInSubWindow

                                if (x + i >= 0 and x + i < w and y - self.maskRange + j >= 0 and y - self.maskRange + j < h):
                                    var[1] += np.power(image_original.getpixel((x + i, y - self.maskRange + j))[0] - mean[1], 2) / self.cellsInSubWindow

                                if (x - self.maskRange + i >= 0 and x - self.maskRange + i < w and y + j >= 0 and y + j < h):
                                    var[2] += np.power(image_original.getpixel((x - self.maskRange + i, y + j))[0] - mean[2], 2) / self.cellsInSubWindow

                                if (x + i < w and y + j < h):
                                    var[3] += np.power(image_original.getpixel((x + i, y + j))[0] - mean[3], 2) / self.cellsInSubWindow

                        min_var_idx = np.where(var == np.amin(var))[0][0]

                        image_copy.putpixel((i, j), (int(mean[min_var_idx]), int(mean[min_var_idx]), int(mean[min_var_idx])))
                        print(z)
            else:
                z = 0
                for i in range(w):
                    for j in range(h):

                        mean_r = np.zeros(4)
                        mean_g = np.zeros(4)
                        mean_b = np.zeros(4)

                        var_r = np.zeros(4)
                        var_g = np.zeros(4)
                        var_b = np.zeros(4)

                        for x in range(self.maskRange + 1):
                            for y in range(self.maskRange + 1):
                                z += 1
                                if(x - self.maskRange + i >= 0 and y - self.maskRange + j >= 0):
                                    mean_r[0] += image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[0] / self.cellsInSubWindow
                                    mean_g[0] += image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[1] / self.cellsInSubWindow
                                    mean_b[0] += image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[2] / self.cellsInSubWindow

                                if(x + i >= 0 and x + i < w and y - self.maskRange + j >= 0 and y - self.maskRange + j < h):
                                    mean_r[1] += image_original.getpixel((x + i, y - self.maskRange + j))[0] / self.cellsInSubWindow
                                    mean_g[1] += image_original.getpixel((x + i, y - self.maskRange + j))[1] / self.cellsInSubWindow
                                    mean_b[1] += image_original.getpixel((x + i, y - self.maskRange + j))[2] / self.cellsInSubWindow

                                if(x - self.maskRange + i >= 0 and x - self.maskRange + i < w and y + j >= 0 and y + j < h):
                                    mean_r[2] += image_original.getpixel((x - self.maskRange + i, y + j))[0] / self.cellsInSubWindow
                                    mean_g[2] += image_original.getpixel((x - self.maskRange + i, y + j))[1] / self.cellsInSubWindow
                                    mean_b[2] += image_original.getpixel((x - self.maskRange + i, y + j))[2] / self.cellsInSubWindow

                                if(x + i < w and y + j < h):
                                    mean_r[3] += image_original.getpixel((x + i, y + j))[0] / self.cellsInSubWindow
                                    mean_g[3] += image_original.getpixel((x + i, y + j))[1] / self.cellsInSubWindow
                                    mean_b[3] += image_original.getpixel((x + i, y + j))[2] / self.cellsInSubWindow

                        for x in range(self.maskRange + 1):
                            for y in range(self.maskRange + 1):
                                z += 1
                                if (x - self.maskRange + i >= 0 and y - self.maskRange + j >= 0):
                                    var_r[0] += np.power(image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[0] - mean_r[0], 2) / self.cellsInSubWindow
                                    var_g[0] += np.power(image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[1] - mean_g[0], 2) / self.cellsInSubWindow
                                    var_b[0] += np.power(image_original.getpixel((x - self.maskRange + i, y - self.maskRange + j))[2] - mean_b[0], 2) / self.cellsInSubWindow

                                if (x + i >= 0 and x + i < w and y - self.maskRange + j >= 0 and y - self.maskRange + j < h):
                                    var_r[1] += np.power(image_original.getpixel((x + i, y - self.maskRange + j))[0] - mean_r[1], 2) / self.cellsInSubWindow
                                    var_g[1] += np.power(image_original.getpixel((x + i, y - self.maskRange + j))[1] - mean_g[1], 2) / self.cellsInSubWindow
                                    var_b[1] += np.power(image_original.getpixel((x + i, y - self.maskRange + j))[2] - mean_b[1], 2) / self.cellsInSubWindow

                                if (x - self.maskRange + i >= 0 and x - self.maskRange + i < w and y + j >= 0 and y + j < h):
                                    var_r[2] += np.power(image_original.getpixel((x - self.maskRange + i, y + j))[0] - mean_r[2], 2) / self.cellsInSubWindow
                                    var_g[2] += np.power(image_original.getpixel((x - self.maskRange + i, y + j))[1] - mean_g[2], 2) / self.cellsInSubWindow
                                    var_b[2] += np.power(image_original.getpixel((x - self.maskRange + i, y + j))[2] - mean_b[2], 2) / self.cellsInSubWindow

                                if (x + i < w and y + j < h):
                                    var_r[3] += np.power(image_original.getpixel((x + i, y + j))[0] - mean_r[3], 2)/ self.cellsInSubWindow
                                    var_g[3] += np.power(image_original.getpixel((x + i, y + j))[1] - mean_g[3], 2) / self.cellsInSubWindow
                                    var_b[3] += np.power(image_original.getpixel((x + i, y + j))[2] - mean_b[3], 2) / self.cellsInSubWindow

                        min_var_r_idx = np.where(var_r == np.amin(var_r))[0][0]
                        min_var_g_idx = np.where(var_g == np.amin(var_g))[0][0]
                        min_var_b_idx = np.where(var_b == np.amin(var_b))[0][0]

                        image_copy.putpixel((i,j),(int(mean_r[min_var_r_idx]), int(mean_g[min_var_g_idx]), int(mean_b[min_var_b_idx])))
                        print(z)

            image_copy.save('kuwahara_result.jpg')
            img = ImageQt(image_copy)

            pixmap_kuwahara = QPixmap(QPixmap.fromImage(img))
            pixmap_kuwahara = pixmap_kuwahara.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_kuwahara)
            print('Koniec')
        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded")
            msg.exec()

    def medianFilter(self):
        if(self.imageLabel.pixmap() is not None):
            image_original = Image.open(self.imagePath, 'r').convert('RGB')
            w, h = image_original.size

            image_copy = image_original.copy()

            idx = int(self.WindowSizeComboBox.currentIndex())
            if (idx == 0): size = 3
            elif (idx == 1): size = 5

            self.maskRange = int(size / 2)
            self.cellsInMask = np.power(size, 2)

            isgray = self.isGray()
            if(isgray):
                z = 0
                for i in range(w):
                    for j in range(h):

                        values_array = np.zeros(self.cellsInMask)
                        iter = 0
                        for x in range(-1 * self.maskRange, self.maskRange + 1):
                            for y in range(-1 * self.maskRange, self.maskRange + 1):
                                z += 1
                                print(z)
                                if (i + x >= 0 and i + x < w and j + y >= 0 and j + y < h):
                                    pix_value = image_original.getpixel((i + x, j + y))
                                    values_array[iter] = pix_value[0]
                                    iter += 1

                        sorted_array = np.sort(values_array)

                        median = int(np.median(sorted_array))

                        image_copy.putpixel((i, j), (median, median, median))
            else:
                z = 0
                for i in range(w):
                    for j in range(h):

                        values_array_r = np.zeros(self.cellsInMask)
                        values_array_g = np.zeros(self.cellsInMask)
                        values_array_b = np.zeros(self.cellsInMask)

                        iter = 0

                        for x in range(-1 * self.maskRange, self.maskRange + 1):
                            for y in range(-1 * self.maskRange, self.maskRange + 1):
                                z += 1
                                print(z)
                                if (i + x >= 0 and i + x < w and j + y >= 0 and j + y < h):
                                    pix_value = image_original.getpixel((i + x, j + y))
                                    values_array_r[iter] = pix_value[0]
                                    values_array_g[iter] = pix_value[1]
                                    values_array_b[iter] = pix_value[2]
                                    iter += 1

                        sorted_array_r = np.sort(values_array_r)
                        sorted_array_g = np.sort(values_array_g)
                        sorted_array_b = np.sort(values_array_b)

                        median_r = int(np.median(sorted_array_r))
                        median_g = int(np.median(sorted_array_g))
                        median_b = int(np.median(sorted_array_b))

                        image_copy.putpixel((i, j), (median_r, median_g, median_b))

            image_copy.save('median_result.jpg')
            img = ImageQt(image_copy)

            pixmap_median = QPixmap(QPixmap.fromImage(img))
            pixmap_median = pixmap_median.scaled(441, 321, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap_median)
            print('Koniec')

        else:
            msg = self.createMessageBox()
            msg.setText("One of the possible problem:\n- There is no image loaded")
            msg.exec()

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        global isSecondWindow
        isSecondWindow = True
        self.setWindowTitle("Window2")
        self.setGeometry(0, 0, img_after.width(), img_after.height())

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, img_after.width(), img_after.height()))
        tmp_pixamp = QPixmap(QPixmap.fromImage(img_after))
        self.label.setPixmap(tmp_pixamp)
        self.label.mousePressEvent = self.getBiggerPixel

    def getBiggerPixel(self, event):
        global isBigger
        global bigger_x
        global bigger_y

        isBigger = True
        bigger_x = event.pos().x()
        bigger_y = event.pos().y()

        c = pixmap_scaled.toImage().pixel(int(bigger_x / ui.scale), int(bigger_y / ui.scale))
        xd = QColor(c).getRgb()

        ui.RtextEdit.setPlainText(str(xd[0]))
        ui.GtextEdit.setPlainText(str(xd[1]))
        ui.BtextEdit.setPlainText(str(xd[2]))

    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        isSecondWindow = False

class MaskWindow(QDialog):

    def __init__(self,_maskSize):
        self.maskSize = _maskSize
        super().__init__()
        self.setWindowTitle("MaskWindow")
        self.setGeometry(175, 175, ((21*self.maskSize)+(29*(self.maskSize - 1)) + 100), (21*self.maskSize) + (19*(self.maskSize-1)) + 150)

        self.SaveMaskButton = QtWidgets.QPushButton(self)
        self.SaveMaskButton.setGeometry(QtCore.QRect(50, 30, 81, 31))
        self.SaveMaskButton.setObjectName("SaveMaskButton")
        self.SaveMaskButton.setText("Save Mask")
        self.SaveMaskButton.clicked.connect(self.saveMask)

        self.ConstructMaskTextEdits(self.maskSize)

    def ConstructMaskTextEdits(self, maskSize):
        numberOfTextEdits = np.power(maskSize, 2)

        fromUp = 90
        fromLeft = 50

        self.maskLineEdits = []

        for i in range(numberOfTextEdits):

            if(i % maskSize == 0 and i != 0):
                fromLeft = 50
                fromUp += 40

            self.MaskLineEdit = QtWidgets.QLineEdit(self)
            self.MaskLineEdit.setGeometry(QtCore.QRect(fromLeft, fromUp, 21, 21))
            self.MaskLineEdit.setObjectName("MaskLineEdit")
            self.MaskLineEdit.setText("1")
            self.MaskLineEdit.setMaxLength(2)

            self.maskLineEdits.append(self.MaskLineEdit)

            fromLeft += 50



    def saveMask(self):

        self.mask = np.zeros((self.maskSize,self.maskSize), dtype=int)
        index = 0
        for i in range(self.maskSize):
            for j in range(self.maskSize):
                self.mask[i][j] = int(self.maskLineEdits[index].text())
                index += 1
        #print(self.mask)

        ui.ConvFilterButton.setEnabled(True)

        self.close()

    def closeEvent(self, *args, **kwargs):
        super(QDialog, self).closeEvent(*args, **kwargs)


if __name__ == "__main__":
    import sys

    global ui
    global isBigger
    global isSecondWindow
    global bigger_x
    global bigger_y
    global x
    global y

    x = -1
    y = -1
    bigger_x = -1
    bigger_y = -1
    isBigger = False
    isSecondWindow = False

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())