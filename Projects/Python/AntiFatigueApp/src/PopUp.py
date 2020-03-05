#!/usr/bin/env python3
import sys
sys.path.append("../UI")
sys.path.append("./")
sys.path.append("./src")

from  PyQt5.QtWidgets import (QMainWindow)

from ui_popup import  *
class PopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AntiFat - Ben je een beetje moe?")
        self.ui = Ui_PopUp()
        self.ui.setupUi(self)
        self.ui.horizontalSlider.valueChanged['int']\
            .connect(self.ui.energy_label_slider_value.update)
