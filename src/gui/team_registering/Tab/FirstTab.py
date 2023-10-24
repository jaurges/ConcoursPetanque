import sys
sys.path.append('.')
from PySide6 import QtCore, QtWidgets, QtGui
import Application


class FirstTab(QtWidgets.QDialog):
    value = QtCore.Signal(list)
    setting = QtCore.Signal()
    def __init__(self):
        super().__init__()  
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        label = QtWidgets.QLabel("Entrez le nom de l'équipe :")
        label_2 = QtWidgets.QLabel("Entrez le nom du club :")
        self.combobox = QtWidgets.QComboBox(self)
        self.pushbutton = QtWidgets.QPushButton("Annuler")
        self.pushbutton_2 = QtWidgets.QPushButton("Ajouter")
        self.tool_button = QtWidgets.QToolButton()
        self.tool_button.setIcon(QtGui.QIcon("images/settings.svg"))
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
        record = [team_name, club_name]
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
        #print("prout")

    @QtCore.Slot()
    def setting_combo(self):
        self.setting.emit()