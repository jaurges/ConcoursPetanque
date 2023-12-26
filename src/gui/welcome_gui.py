import sys

from PySide6 import QtCore, QtWidgets, QtGui


class WelcomeGui(QtWidgets.QWidget):
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")

        self.button = QtWidgets.QPushButton("Suivant")
        self.button2 = QtWidgets.QPushButton("Suivant")
        self.text = QtWidgets.QLabel("Créer un nouveau concours",
                                     alignment=QtCore.Qt.AlignCenter)
        self.text2 = QtWidgets.QLabel("Ouvrir un ancien concours",
                                     alignment=QtCore.Qt.AlignCenter)
        frame1 = QtWidgets.QFrame()
        frame2 = QtWidgets.QFrame()

        self.layout_base = QtWidgets.QHBoxLayout(self)
        self.layout_left = QtWidgets.QVBoxLayout()
        self.layout_right = QtWidgets.QVBoxLayout()

        frame1.setStyleSheet("""
            QFrame {
                background-color: #b4ff8f; /* Couleur de fond */
            }
        """)
        frame1.setLayout(self.layout_left)
        frame2.setStyleSheet("""
            QFrame {
                background-color: #8fb8ff; /* Couleur de fond */
            }
        """)
        frame2.setLayout(self.layout_right)
        
        #self.layout_left.addWidget(frame1)
        self.layout_left.addWidget(self.text)
        self.layout_left.addWidget(self.button)
        #self.layout_right.addWidget(frame2)
        self.layout_right.addWidget(self.text2)
        self.layout_right.addWidget(self.button2)
        self.layout_base.addWidget(frame1)
        self.layout_base.addWidget(frame2)

        self.button.clicked.connect(self.open_next)

    def open_next(self):
        self.opened.emit()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = WelcomeGui()
    widget.resize(480, 360)
    widget.show()

    sys.exit(app.exec())
