import sys
#from ErroGui import ErrorGui

sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from data.database_handler import DatabaseHandler


'''class ParametersGui(QtWidgets.QWidget):

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

        self.pushbutton_2.clicked.connect(self.saving)

    @QtCore.Slot()
    def saving(self):
        app = Application()
        name = self.lineEdit.text()
        date = self.calendar.selectedDate()
        formatted_date = date.toString("yyyy-M-d")
        play_mod = ""
        location = self.lineEdit2.text()
        if self.radiobutton.isChecked():
            play_mod = "Doublette"
        if self.radiobutton_2.isChecked():
            play_mod = "Triplette"
        try:
            app.clicked_btn(name, formatted_date, play_mod, location)
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
        self.database_handler = DatabaseHandler("databasev2.db")

    def clicked_btn(self, name: str, date: str, play_mod: str, location: str):
        self.database_handler.create_competition(name, date, play_mod, location)
        print(name, date, play_mod)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = ParametersGui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())'''

from PySide6 import QtWidgets, QtCore

class ParametersGui(QtWidgets.QWidget):
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parameters")

        self.back_button = QtWidgets.QPushButton("Retour")
        self.button = QtWidgets.QPushButton("Aller")
        self.text = QtWidgets.QLabel("Paramètres de configuration",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.back_button)
        self.layout.addWidget(self.button)

        self.back_button.clicked.connect(self.open_previous)
        self.button.clicked.connect(self.open_next)

    def open_previous(self):
        self.parent_widget.show()
        self.close()

    def open_next(self):
        self.opened.emit()
        #self.parent_widget.close()
        self.close()

