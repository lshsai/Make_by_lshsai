import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import test_sum as tsum

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("test_1.ui", self)
        self.ui.show()


    @pyqtSlot()  # import 버튼 클릭 시
    def sum(self):
        try:
            a = int(self.ui.input_A.text())
            b = int(self.ui.input_B.text())
            result = str(tsum.sum(a,b))

        except:
            result = "두개를 더할수 없습니다"

        self.ui.Sum_result.setText(result)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())