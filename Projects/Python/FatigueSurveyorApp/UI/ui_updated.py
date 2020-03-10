# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_updated.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class QJumpSlider(QtWidgets.QSlider):
    def __init__(self, parent=None):
        super(QJumpSlider, self).__init__(parent)

    def mousePressEvent(self, event):
        # Jump to click position
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))

    def mouseMoveEvent(self, event):
        # Jump to pointer position while moving
        self.setValue(QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.Dialog =Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.setGeometry(QtCore.QRect(0, 0, 531, 543))
        self.Dialog.setMinimumSize(QtCore.QSize(531, 319))
        self.Dialog.setWindowIcon(QIcon("/usr/share/pixmaps/app_icon.png"))
        self.Dialog.setMaximumSize(QtCore.QSize(531, 543))
        self.Dialog.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);")
        self.timeout_frame =QtWidgets.QFrame(Dialog)
        self.timeout_frame.setGeometry(QtCore.QRect(0, 320, 531, 221))
        self.timeout_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeout_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timeout_frame.setObjectName("timeout_frame")

        self.timeout_frame_label =QtWidgets.QLabel(self.timeout_frame)
        self.timeout_frame_label.setGeometry(QtCore.QRect(0, 60, 531, 71))
        self.timeout_frame_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timeout_frame_label.setObjectName("timeout_frame_label")
        self.timeout_frame.hide()
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 320, 531, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.energy_label_excellent = QtWidgets.QLabel(self.frame)
        self.energy_label_excellent.setGeometry(QtCore.QRect(430, 80, 67, 17))
        self.energy_label_excellent.setAlignment(QtCore.Qt.AlignCenter)
        self.energy_label_excellent.setObjectName("energy_label_excellent")
        self.energy_label_question = QtWidgets.QLabel(self.frame)
        self.energy_label_question.setGeometry(QtCore.QRect(90, 50, 341, 20))
        self.energy_label_question.setObjectName("energy_label_question")
        self.energy_label_bad = QtWidgets.QLabel(self.frame)
        self.energy_label_bad.setGeometry(QtCore.QRect(10, 80, 67, 17))
        self.energy_label_bad.setAlignment(QtCore.Qt.AlignCenter)
        self.energy_label_bad.setObjectName("energy_label_bad")
        self.horizontalSlider = QJumpSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 110, 421, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        #self.horizontalSlider.setMouseTracking(True)

        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.energy_label_slider_value = QtWidgets.QLabel(self.frame)
        self.energy_label_slider_value.setGeometry(QtCore.QRect(220, 80, 67, 20))
        self.energy_label_slider_value.setAlignment(QtCore.Qt.AlignCenter)
        self.energy_label_slider_value.setObjectName("energy_label_slider_value")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(270, 130, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.image_label = QtWidgets.QLabel(Dialog)
        self.image_label.setEnabled(True)
        self.image_label.setGeometry(QtCore.QRect(110, 10, 300, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QtCore.QSize(300, 300))
        self.image_label.setMaximumSize(QtCore.QSize(300, 300))
        self.image_label.setBaseSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.image_label.setFont(font)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 520, 501, 91))
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        # self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fatigue Surveyor - Ben je een beetje moe?"))
        self.energy_label_excellent.setText(_translate("Dialog", "Energiek"))
        self.energy_label_question.setText(_translate("Dialog", "Op een schaal van 0 tot 10 hoe energiek ben je?"))
        self.energy_label_bad.setText(_translate("Dialog", "Moe"))
        self.energy_label_slider_value.setText(_translate("Dialog", "0"))
        self.image_label.setText(_translate("Dialog", ""))
        self.timeout_frame_label.setText("")

    def setWindowIcon(self, param):
            pass

