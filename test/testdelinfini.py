from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.tabWidget = QtWidgets.QTabWidget()
        self.listWidget = QtWidgets.QListWidget()

        self.first_tab = FirstTab()
        self.second_tab = SecondTab()

        self.first_tab.value.connect(self.fill)

        self.tabWidget.addTab(self.first_tab, "first tab")
        self.tabWidget.addTab(self.second_tab, "second tab")

        self.layout = QtWidgets.QHBoxLayout(self)

        self.layout.addWidget(self.tabWidget)
        self.layout.addWidget(self.listWidget)

    @QtCore.Slot(str)
    def fill(self, message):
        self.listWidget.addItem(message)

class FirstTab(QtWidgets.QWidget):
    value = QtCore.Signal(str)
    def __init__(self):
        super().__init__()
        self.lineEdit = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("add")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.clicked)

    @QtCore.Slot()
    def clicked(self):
        self.value.emit(self.lineEdit.text())

class SecondTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec())