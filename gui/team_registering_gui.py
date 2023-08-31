import sys
sys.path.append(".")

from PySide6 import QtCore, QtWidgets, QtGui
#from object.object import Team
from data.database_handler import DatabaseHandler


class TeamRegistering(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")

        self.first_tab = FirstTab()
        second_tab = SecondTab()
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.first_tab, "manual")
        tab_widget.addTab(second_tab, "loading")

        self.first_tab.value.connect(self.fill)
        self.first_tab.setting.connect(self.show_setcombo)

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
    
    @QtCore.Slot()
    def show_setcombo(self):
        win = SettingCombo()
        win.club.connect(self.first_tab.addItemtocombo)
        win.exec()


class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db")

    def register_team(self, name: str, club: str):
        self.database_handler.create_team(name, club)

class FirstTab(QtWidgets.QDialog):
    value = QtCore.Signal(str)
    setting = QtCore.Signal()
    def __init__(self):
        super(FirstTab, self).__init__()  
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        label = QtWidgets.QLabel("Entrez le nom de l'équipe :")
        label_2 = QtWidgets.QLabel("Entrez le nom du club :")
        self.combobox = QtWidgets.QComboBox(self)
        self.pushbutton = QtWidgets.QPushButton("Annuler")
        self.pushbutton_2 = QtWidgets.QPushButton("Ajouter")
        self.tool_button = QtWidgets.QToolButton()
        self.tool_button.setIcon(QtGui.QIcon("icon/settings.svg"))
        spacer_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        spacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.combobox.addItem("Asc Cordemais")
        self.combobox.addItem("St Etienne")
        self.combobox.addItem("Bouée")

        layout_1 = QtWidgets.QVBoxLayout()
        layout_2 = QtWidgets.QVBoxLayout()
        layout_button_1 = QtWidgets.QHBoxLayout()
        layout_combobox = QtWidgets.QHBoxLayout()
        
        layout_base = QtWidgets.QVBoxLayout(self)

        layout_1.addWidget(label)
        layout_1.addWidget(self.lineEdit)
        layout_combobox.addWidget(self.combobox)
        layout_combobox.addWidget(self.tool_button)
        layout_2.addWidget(label_2)
        layout_2.addWidget(self.lineEdit_2)
        layout_2.addLayout(layout_combobox)
        layout_button_1.addWidget(self.pushbutton)
        layout_base.addSpacerItem(spacer_1)
        layout_base.addLayout(layout_2)
        layout_base.addSpacerItem(spacer_2)
        layout_base.addLayout(layout_button_1)

        self.combobox.activated.connect(self.club_name)

        self.pushbutton_2.clicked.connect(self.register_team)
        self.pushbutton_2.clicked.connect(self.value_added)
        self.pushbutton_2.clicked.connect(self.reset)
        self.pushbutton.clicked.connect(self.reset)
        self.tool_button.clicked.connect(self.setting_combo)

    def register_team(self):
        team = self.lineEdit.text()
        club = self.lineEdit_2.text()
        app = Application()

        app.register_team(team, club)
    
    @QtCore.Slot()
    def value_added(self):
        team_name = self.lineEdit.text()
        club_name = self.lineEdit_2.text()
        record = f"{team_name} {club_name}"
        self.value.emit(record)

    def reset(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def club_name(self):
        club_name = self.combobox.currentText()
        self.lineEdit_2.setText(club_name)
    
    @QtCore.Slot(str)
    def addItemtocombo(self, text):
        self.combobox.addItem(text)
        print("prout")


    @QtCore.Slot()
    def setting_combo(self):
        self.setting.emit()

class SecondTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class SettingCombo(QtWidgets.QDialog):
    club = QtCore.Signal(str)
    def __init__(self):
        super().__init__()
        #firsttab = FirstTab()
        #self.club.connect(firsttab.addItemtocombo)

        label = QtWidgets.QLabel("Ajouter un nom de club")
        self.lineEdit = QtWidgets.QLineEdit()
        button_1 = QtWidgets.QPushButton("Valider")
        button_2 = QtWidgets.QPushButton("Annuler")
        layout = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.lineEdit)
        layout_button.addWidget(button_2)
        layout_button.addWidget(button_1)
        layout.addLayout(layout_button)

        button_1.clicked.connect(self.btn)

    @QtCore.Slot()
    def btn(self):
        self.club.emit(self.lineEdit.text())
        self.lineEdit.clear()
        print("prout")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TeamRegistering()

    widget.resize(500, 500)
    widget.show()

    sys.exit(app.exec())
