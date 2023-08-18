from PySide6 import QtWidgets
import sys


class Widget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        mainLayout = QtWidgets.QVBoxLayout(self)

        testWidget = QtWidgets.QFrame()
        #testWidget.setFixedSize(100,100)
        testWidget.setObjectName("myWidget")
        testWidget.setStyleSheet("#myWidget {background-color:red;}")

        testLayout = QtWidgets.QVBoxLayout()

        testWidget.setLayout(testLayout)

        but = QtWidgets.QPushButton('TEST')
        testLayout.addWidget(but)

        mainLayout.addWidget(testWidget)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    instance_1 = Widget()
    instance_1.show()
    sys.exit(app.exec_())