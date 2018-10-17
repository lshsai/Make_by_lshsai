# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import random

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("HWorld.ui", self)
        self.ui.show()
        self.A = ['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png']

    @pyqtSlot()
    def slot_1st(self):
        self.B = self.A[random.randint(0, 5)]
        self.img = QPixmap(self.B)
        self.ui.label2.setPixmap(self.img)

    @pyqtSlot()
    def slot_2nd(self):
        self.img = QPixmap(self.A[random.randint(1, 6)])
        self.ui.label2.setPixmap(self.img)

    @pyqtSlot()
    def slot_3rd(self):
        sys.exit(app.exec())




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())