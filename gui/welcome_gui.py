import sys
from PySide6 import QtCore, QtWidgets, QtGui


class WelcomeGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")

        self.button = QtWidgets.QPushButton("Suivant")
        self.text = QtWidgets.QLabel("Créer un nouveau concours",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = WelcomeGui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())
