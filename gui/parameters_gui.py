import sys
#from ErroGui import ErrorGui

sys.path.append("..")
from PySide6 import QtCore, QtWidgets, QtGui
from object.object import Competition


class ParametersGui(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parameters")

        self.label = QtWidgets.QLabel("Entrez le nom du concours :")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.label_2 = QtWidgets.QLabel("Entrez la date du concours :")
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
        self.layout_general.addLayout(self.layout_radiobutton)
        self.layout_general.addWidget(self.label_2)
        self.layout_general.addWidget(self.calendar)
        self.layout_general.addLayout(self.layout_pushbutton)

        self.pushbutton_2.clicked.connect(self.saving)

    @QtCore.Slot()
    def saving(self):
        app = Application()
        name = self.lineEdit.text()
        date = self.calendar.selectedDate()
<<<<<<< HEAD
        formatted_date = date.toString("yyyy-M-d")
        play_mod = ""
        location = self.lineEdit2.text()
=======
>>>>>>> parent of 4cf90b7 (ajout location les conflits sont réglé a l'aide de ses con,naissances)
        if self.radiobutton.isChecked():
            play_mod = "Doublette"
        if self.radiobutton_2.isChecked():
            play_mod = "Triplette"
        try:
<<<<<<< HEAD
            app.clicked_btn(name, formatted_date, play_mod, location)
=======
            app.clicked_btn(name, date, play_mod)
>>>>>>> parent of 4cf90b7 (ajout location les conflits sont réglé a l'aide de ses con,naissances)
        except UnboundLocalError:
            erroGui = ErrorGui()
            erroGui.resize(400, 100)
            erroGui.show()


class ErrorGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("Veuillez entrer le mode de jeu", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)


class Application:
    def __init__(self):
        self.database_handler = Competition("database.db")

<<<<<<< HEAD
    def clicked_btn(self, name: str, date: str, play_mod: str, location: str):
        self.database_handler.create_competition(name, date, play_mod, location)
=======
    def clicked_btn(self, name: str, date: str, play_mod: str):
        self.database_handler.save_parameters(name, date, play_mod)
>>>>>>> parent of 4cf90b7 (ajout location les conflits sont réglé a l'aide de ses con,naissances)
        print(name, date, play_mod)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = ParametersGui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())
