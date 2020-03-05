# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_popup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 235)
        Dialog.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                             "gridline-color: rgb(0, 0, 0);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 190, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 150, 421, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSliderPosition(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setRange(0, 10)

        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        # self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.energy_label_bad = QtWidgets.QLabel(Dialog)
        self.energy_label_bad.setGeometry(QtCore.QRect(50, 120, 67, 17))
        self.energy_label_bad.setAlignment(QtCore.Qt.AlignCenter)
        self.energy_label_bad.setObjectName("energy_label_bad")
        self.energy_label_slider_value = QtWidgets.QLabel(Dialog)
        self.energy_label_slider_value.setGeometry(QtCore.QRect(260, 120, 67, 20))
        self.energy_label_slider_value.setAlignment(QtCore.Qt.AlignCenter)
        self.energy_label_slider_value.setObjectName("energy_label_slider_value")
        self.energy_label_excellent = QtWidgets.QLabel(Dialog)
        self.energy_label_excellent.setGeometry(QtCore.QRect(470, 120, 67, 17))
        self.energy_label_excellent.setAlignment(QtCore.Qt.AlignCenter)
        self.energy_label_excellent.setObjectName("energy_label_excellent")
        self.energy_label_question = QtWidgets.QLabel(Dialog)
        self.energy_label_question.setGeometry(QtCore.QRect(130, 90, 341, 20))
        self.energy_label_question.setObjectName("energy_label_question")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 80, 501, 91))
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.buttonBox.raise_()
        self.horizontalSlider.raise_()
        self.energy_label_bad.raise_()
        self.energy_label_slider_value.raise_()
        self.energy_label_excellent.raise_()
        self.energy_label_question.raise_()

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        # self.buttonBox.rejected.connect(Dialog.reject)
        self.horizontalSlider.valueChanged['int'].connect(self.update)
        # self.horizontalSlider
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def update(self):
        self.energy_label_slider_value.setText(str(self.horizontalSlider.value()))

    def slider_pressed(self):
        add_to_slider_val = 1
        if self.horizontalSlider.value() == 10:
            add_to_slider_val = -1
        if self.horizontalSlider.value() == 0:
            add_to_slider_val = 1

        self.horizontalSlider.setValue(self.horizontalSlider.value() + add_to_slider_val)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.energy_label_bad.setText(_translate("Dialog", "Moe"))
        self.energy_label_slider_value.setText(_translate("Dialog", "0"))
        self.energy_label_excellent.setText(_translate("Dialog", "Energiek"))
        self.energy_label_question.setText(_translate("Dialog", "Op een schaal van 0 tot en met 10 hoe energiek ben je?"))
