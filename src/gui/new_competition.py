import sys

sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class NewCompetition(QtWidgets.QWidget):
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parameters")

        self.label = QtWidgets.QLabel("Entrez le nom du concours :")
        self.label_2 = QtWidgets.QLabel("Entrez la date du concours :")
        self.label_3 = QtWidgets.QLabel("Entrez la localisation du concours :")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.radiobutton = QtWidgets.QRadioButton(self)
        self.radiobutton_2 = QtWidgets.QRadioButton(self)
        self.pushbutton = QtWidgets.QPushButton(self)
        self.pushbutton_2 = QtWidgets.QPushButton(self)
        self.calendar = QtWidgets.QCalendarWidget(self)

        self.radiobutton.setText("Doublette")
        self.radiobutton_2.setText("Triplette")
        self.pushbutton.setText("Précédent")
        self.pushbutton_2.setText("Suivant")

        self.layout_radiobutton = QtWidgets.QHBoxLayout()
        # self.layout_radiobutton.setParent()
        self.layout_pushbutton = QtWidgets.QHBoxLayout()
        self.layout_general = QtWidgets.QVBoxLayout(self)

        self.layout_radiobutton.addWidget(self.radiobutton)
        self.layout_radiobutton.addWidget(self.radiobutton_2)
        self.layout_pushbutton.addWidget(self.pushbutton)
        self.layout_pushbutton.addWidget(self.pushbutton_2)
        self.layout_general.addWidget(self.label)
        self.layout_general.addWidget(self.lineEdit)
        self.layout_general.addWidget(self.label_3)
        self.layout_general.addWidget(self.lineEdit2)
        self.layout_general.addLayout(self.layout_radiobutton)
        self.layout_general.addWidget(self.label_2)
        self.layout_general.addWidget(self.calendar)
        self.layout_general.addLayout(self.layout_pushbutton)

        self.pushbutton.clicked.connect(self.open_previous)
        self.pushbutton_2.clicked.connect(self.saving)

    def open_previous(self):
        self.parent_widget.show()
        self.close()

    @QtCore.Slot()
    def saving(self):
        app = Application()
        name = self.lineEdit.text()
        date = self.calendar.selectedDate()
        formatted_date = date.toString("yyyy-M-d")
        play_mod = None
        location = self.lineEdit2.text()
        if self.radiobutton.isChecked():
            play_mod = "Doublette"
        if self.radiobutton_2.isChecked():
            play_mod = "Triplette"
        if play_mod == None:
            erroGui = ErrorGui()
            erroGui.resize(400, 100)
            erroGui.exec()
        else:
            app.new_competition(name, formatted_date, play_mod, location)
            app.set_competition_index([name, formatted_date, play_mod, location])
            self.opened.emit()
            self.close()


class ErrorGui(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("Veuillez entrer le mode de jeu", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = NewCompetition()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())