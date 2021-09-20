import sys

keyword = ""

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication

keyInput_ui = uic.loadUiType("autofinder_keyInput.ui")[0]
class WindowClass(QMainWindow, keyInput_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.changeTextFunction)
        self.pushButton_ok.clicked.connect(QCoreApplication.instance().quit)
    def changeTextFunction(self):
        global keyword
        keyword = self.lineEdit_searchKeyword.text()
        


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

    

keyInput_ui = uic.loadUiType("autofinder_keyInput.ui")[0]
class WindowClass(QMainWindow, keyInput_ui) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.changeTextFunction)
        self.pushButton_ok.clicked.connect(QCoreApplication.instance().quit)
    def changeTextFunction(self):
        global keyword
        keyword = self.lineEdit_searchKeyword.text()




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()