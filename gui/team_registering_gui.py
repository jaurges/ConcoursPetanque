import sys
sys.path.append(".")

from PySide6 import QtCore, QtWidgets, QtGui
#from object.object import Team
from data.database_handler import DatabaseHandler


class Team_registering(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.label = QtWidgets.QLabel("Entrez le nom de l'équipe :")
        self.label_2 = QtWidgets.QLabel("Entrez le nom du club :")
        self.combobox = QtWidgets.QComboBox(self)
        self.pushbutton = QtWidgets.QPushButton("Annuler")
        self.pushbutton_2 = QtWidgets.QPushButton("Ajouter")
        self.pushbutton_3 = QtWidgets.QPushButton("Annuler")
        self.pushbutton_4 = QtWidgets.QPushButton("Suivant")
        self.listWidget = QtWidgets.QListWidget(self)

        #self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #   self.spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout_2 = QtWidgets.QVBoxLayout()
        self.layout_3 = QtWidgets.QHBoxLayout()
        self.layout_4 = QtWidgets.QHBoxLayout()
        self.layout_base = QtWidgets.QVBoxLayout(self)
        self.layout_left = QtWidgets.QVBoxLayout()
        self.layout_middle = QtWidgets.QHBoxLayout()

        self.combobox.addItem("Asc Cordemais")
        self.combobox.addItem("St Etienne")
        self.combobox.addItem("Bouée")

        self.layout_init()

        self.layout.addSpacing(100)
        self.layout_2.addSpacing(100)

        self.signal_init()

    def layout_init(self):
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        #self.layout.addWidget(self.spacerItem1)
        self.layout_2.addWidget(self.label_2)
        self.layout_2.addWidget(self.lineEdit_2)
        self.layout_2.addWidget(self.combobox)
        #self.layout_2.addWidget(self.spacerItem2)
        self.layout_3.addWidget(self.pushbutton)
        self.layout_3.addWidget(self.pushbutton_2)
        self.layout_4.addWidget(self.pushbutton_3)
        self.layout_4.addWidget(self.pushbutton_4)
        self.layout_left.addLayout(self.layout)
        self.layout_left.addLayout(self.layout_2)
        self.layout_left.addLayout(self.layout_3)
        self.layout_middle.addLayout(self.layout_left)
        self.layout_middle.addWidget(self.listWidget)
        self.layout_base.addLayout(self.layout_middle)
        self.layout_base.addLayout(self.layout_4)

    def signal_init(self):
        self.combobox.activated.connect(self.club_name)
        self.pushbutton_2.clicked.connect(self.register_team)
        self.pushbutton_2.clicked.connect(self.print_list)
        self.pushbutton_2.clicked.connect(self.reset)
        self.pushbutton.clicked.connect(self.reset)
        
    @QtCore.Slot()
    def club_name(self):
        club_name = self.combobox.currentText()
        self.lineEdit_2.setText(club_name)

    def register_team(self):
        team = self.lineEdit.text()
        club = self.lineEdit_2.text()
        app = Application()

        app.register_team(team, club)

    def reset(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def print_list(self):
        team_name = self.lineEdit.text()
        club_name = self.lineEdit_2.text()
        record = str(team_name + " " + club_name)
        self.listWidget.addItem(record)


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db")

    def register_team(self, team: str, club: str):
        self.database_handler.create_team(team, club)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Team_registering()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())
