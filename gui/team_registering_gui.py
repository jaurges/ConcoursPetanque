import sys
sys.path.append(".")

from PySide6 import QtCore, QtWidgets, QtGui
#from object.object import Team
from data.database_handler import DatabaseHandler
from PySide6.QtCore import Signal, Slot


class TeamRegistering(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")

        first_tab = FirstTab()
        second_tab = SecondTab()
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(first_tab, "manual")
        tab_widget.addTab(second_tab, "loading")

        first_tab.value.connect(self.fill)

        pushbutton_3 = QtWidgets.QPushButton("Annuler")
        pushbutton_4 = QtWidgets.QPushButton("Suivant")
        self.listWidget = QtWidgets.QListWidget()

        layout_base = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout_middle = QtWidgets.QHBoxLayout()

        layout_button.addWidget(pushbutton_3)
        layout_button.addWidget(pushbutton_4)
        layout_middle.addWidget(tab_widget)
        layout_middle.addWidget(self.listWidget)
        layout_base.addLayout(layout_middle)
        layout_base.addLayout(layout_button)
    
    @QtCore.Slot(str)
    def fill(self, message):
        self.listWidget.addItem(message)
        print("atteint")


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db")

    def register_team(self, name: str, club: str):
        self.database_handler.create_team(name, club)

class FirstTab(QtWidgets.QDialog):
    value = QtCore.Signal(str)
    def __init__(self):
        super(FirstTab, self).__init__()
        
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        label = QtWidgets.QLabel("Entrez le nom de l'équipe :")
        label_2 = QtWidgets.QLabel("Entrez le nom du club :")
        self.combobox = QtWidgets.QComboBox(self)
        self.pushbutton = QtWidgets.QPushButton("Annuler")
        self.pushbutton_2 = QtWidgets.QPushButton("Ajouter")
        spacer_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.combobox.addItem("Asc Cordemais")
        self.combobox.addItem("St Etienne")
        self.combobox.addItem("Bouée")

        layout_1 = QtWidgets.QVBoxLayout()
        layout_2 = QtWidgets.QVBoxLayout()
        layout_button_1 = QtWidgets.QHBoxLayout()
        
        layout_base = QtWidgets.QVBoxLayout(self)

        layout_1.addWidget(label)
        layout_1.addWidget(self.lineEdit)
        layout_2.addWidget(label_2)
        layout_2.addWidget(self.lineEdit_2)
        layout_2.addWidget(self.combobox)
        layout_button_1.addWidget(self.pushbutton)
        layout_button_1.addWidget(self.pushbutton_2)

        layout_base.addLayout(layout_1)
        layout_base.addSpacerItem(spacer_1)
        layout_base.addLayout(layout_2)
        layout_base.addSpacerItem(spacer_2)
        layout_base.addLayout(layout_button_1)

        self.combobox.activated.connect(self.club_name)

        self.pushbutton_2.clicked.connect(self.register_team)
        self.pushbutton_2.clicked.connect(self.value_added)
        self.pushbutton_2.clicked.connect(self.reset)
        self.pushbutton.clicked.connect(self.reset)

    def register_team(self):
        team = self.lineEdit.text()
        club = self.lineEdit_2.text()
        app = Application()

        app.register_team(team, club)
    @QtCore.Slot()
    def value_added(self):
        print("launch")
        team_name = self.lineEdit.text()
        club_name = self.lineEdit_2.text()
        record = f"{team_name} {club_name}"
        self.value.emit(record)
        print(record)

    def reset(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def club_name(self):
        club_name = self.combobox.currentText()
        self.lineEdit_2.setText(club_name)

    def return_clubteam(self):
        team = self.lineEdit.text()
        club = self.lineEdit_2.text()
        return [team, club]


class SecondTab(QtWidgets.QWidget):
    def __init__(self):
        super(SecondTab, self).__init__()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    team_registering = TeamRegistering()
    '''firsttab = FirstTab()
    firsttab.value_added.connect(team_registering.value_added_func)'''

    team_registering.resize(360, 480)
    team_registering.show()

    sys.exit(app.exec())
