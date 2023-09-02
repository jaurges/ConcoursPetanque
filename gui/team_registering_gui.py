import sys
sys.path.append(".")
import re
from PySide6 import QtCore, QtWidgets, QtGui
#from object.object import Team
from data.database_handler import DatabaseHandler


class TeamRegistering(QtWidgets.QWidget):
    header_finder = QtCore.Signal(int)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")
        self.team_data = {}
        self.index_club = {}
        self.n = 0

        self.first_tab = FirstTab()
        self.second_tab = SecondTab()
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.first_tab, "manuel")
        tab_widget.addTab(self.second_tab, "générer")

        self.first_tab.value.connect(self.fill)
        self.first_tab.setting.connect(self.show_setcombo)
        self.second_tab.column.connect(self.set_col_count)
        self.second_tab.row.connect(self.set_row_count)
        self.second_tab.header.connect(self.fill_header_automat)
        self.second_tab.header_find_first.connect(self.get_column_index_by_name)
        self.second_tab.value_automat.connect(self.fill_automat)
        self.header_finder.connect(self.second_tab.set_team_forreal)

        pushbutton_3 = QtWidgets.QPushButton("Annuler")
        pushbutton_4 = QtWidgets.QPushButton("Suivant")
        self.table = QtWidgets.QTableWidget()

        layout_base = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout_middle = QtWidgets.QHBoxLayout()

        layout_button.addWidget(pushbutton_3)
        layout_button.addWidget(pushbutton_4)
        layout_middle.addWidget(tab_widget)
        layout_middle.addWidget(self.table)
        layout_base.addLayout(layout_middle)
        layout_base.addLayout(layout_button)
    
    @QtCore.Slot(list)
    def fill(self, list):
        team_name = list[0]
        club_name = list[1]
        if club_name in self.team_data:
            pass
        else:
            #print("\nprout\n")
            self.index_club[club_name] = self.n
            self.n = self.n + 1
        self.team_data.setdefault(club_name, []).append(team_name)
        row = len(self.team_data[club_name]) -1
        column = self.index_club[club_name]
        item = QtWidgets.QTableWidgetItem(team_name)
        x = 0
        for _ in self.team_data[club_name]:
            x = x + 1
        self.table.setColumnCount(self.n)
        self.table.setRowCount(x)
        self.table.setHorizontalHeaderItem(column, QtWidgets.QTableWidgetItem(club_name))
        self.table.setItem(row, column, item)
        '''print(row)
        print(column)
        print(team_name)
        print(club_name)
        print(self.team_data)
        print(self.index_club)
        print("\n")'''
                
    @QtCore.Slot()
    def show_setcombo(self):
        win = SettingCombo()
        win.club.connect(self.first_tab.addItemtocombo)
        win.exec()
    
    @QtCore.Slot(int)
    def set_col_count(self, num):
        self.table.setColumnCount(num)

    @QtCore.Slot(int)
    def set_row_count(self, num):
        self.table.setRowCount(num)

    @QtCore.Slot(dict)
    def fill_automat(self, dicto):
        for i in dicto:
            #print(i)
            for j in dicto[i]:
                #print(j)
                self.table.setItem(j[0], j[1], QtWidgets.QTableWidgetItem(j[2]))
            

    @QtCore.Slot(list)
    def fill_header_automat(self, ls):
        #print(ls)
        self.table.setHorizontalHeaderItem(ls[0]-1, QtWidgets.QTableWidgetItem(ls[1]))

    @QtCore.Slot(str)
    def get_column_index_by_name(self, nom_colonne):
        header = self.table.horizontalHeaderItem(0)
        colonne = ""
        for colonne in range(self.table.columnCount()):
            try:
                if header.text() == nom_colonne:
                    column = int(colonne)
                    break
            except AttributeError:
                pass
            header = self.table.horizontalHeaderItem(colonne + 1)
        self.header_finder.emit(column)

class Application:
    def __init__(self):
        self.database_handler = DatabaseHandler("databasev2.db")

    def register_team(self, name: str, club: str):
        self.database_handler.create_team(name, club)

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
        print("prout")

    @QtCore.Slot()
    def setting_combo(self):
        self.setting.emit()

class SecondTab(QtWidgets.QWidget):
    column = QtCore.Signal(int)
    row = QtCore.Signal(int)
    header = QtCore.Signal(list)
    header_find_first = QtCore.Signal(str)
    value_automat = QtCore.Signal(dict)
    def __init__(self):
        super().__init__()
        label1 = QtWidgets.QLabel("Entrez le nombre de club : ")
        label2 = QtWidgets.QLabel("Nombre : ")
        label3 = QtWidgets.QLabel("Nom : ")
        self.spinbox1 = QtWidgets.QSpinBox()
        self.spinbox2 = QtWidgets.QSpinBox()
        spacer1 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        spacer4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        button1 = QtWidgets.QPushButton("Annuler")
        button2 = QtWidgets.QPushButton("Valider")
        self.lineEdit = QtWidgets.QLineEdit()
        self.combobox = QtWidgets.QComboBox()

        layout_base = QtWidgets.QVBoxLayout(self)
        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        layout3 = QtWidgets.QHBoxLayout()
        layout4 = QtWidgets.QHBoxLayout()
        layout_top = QtWidgets.QVBoxLayout()
        layout_bottom = QtWidgets.QVBoxLayout()
        layout_button = QtWidgets.QHBoxLayout()

        layout1.addWidget(label1)
        layout1.addSpacerItem(spacer1)
        layout1.addWidget(self.spinbox1)

        layout_top.addLayout(layout1)
        layout_top.addLayout(layout2)

        layout_button.addWidget(button1)
        layout_button.addWidget(button2)

        layout3.addWidget(label3)
        layout3.addWidget(self.lineEdit)

        layout4.addWidget(label2)
        layout4.addWidget(self.spinbox2)

        layout_bottom.addWidget(self.combobox)
        layout_bottom.addLayout(layout3)
        layout_bottom.addLayout(layout4)
        layout_bottom.addSpacerItem(spacer4)
        layout_bottom.addLayout(layout_button)

        layout_base.addLayout(layout_top)
        layout_base.addSpacerItem(spacer3)
        layout_base.addLayout(layout_bottom)

        self.spinbox1.valueChanged.connect(self.col_count)
        self.spinbox1.valueChanged.connect(self.set_club)
        self.spinbox2.valueChanged.connect(self.row_count)
        self.spinbox2.valueChanged.connect(self.set_team)
        self.combobox.currentIndexChanged.connect(self.print_in_edit)
        self.lineEdit.editingFinished.connect(self.print_header)

        self.ls_row = []
        self.dicto_team_real = {}
        


    @QtCore.Slot()
    def col_count(self):
        value = self.spinbox1.value()
        self.column.emit(value)
    
    @QtCore.Slot()
    def row_count(self):
        value = self.spinbox2.value()
        self.ls_row.append(value)
        num = max(self.ls_row)
        num1  = int(num)
        #self.j = self.j - 1
        self.row.emit(num1)
        #print(f"\n{num1}\n")

    def set_club(self):
        value = self.spinbox1.value()
        club_name = f"club{value}"
        self.combobox.addItem(club_name)
    
    def print_in_edit(self):
        value = self.combobox.currentText()
        self.lineEdit.setText(value)

    @QtCore.Slot()
    def print_header(self):
        ls = []
        num = str
        txt = self.combobox.currentText()
        for c in txt:
            if c.isdigit():
                num = c
        ls.append(int(num))
        ls.append(self.lineEdit.text())
        self.header.emit(ls)
    
    @QtCore.Slot()
    def set_team(self):
        self.header_find_first.emit(self.lineEdit.text())
        
    @QtCore.Slot(int)
    def set_team_forreal(self, col):
        x = self.spinbox2.value()
        y = self.lineEdit.text()
        ls_max = []
        ls_max_1 = []
        max_num = 0
        max_num_y = 0
        if not self.dicto_team_real:
            pass
        else:
            for key in self.dicto_team_real:
                for team in self.dicto_team_real[key]:
                    pattern = r'\d+\.\d+|\d+'
                    team = str(team)
                    correspondences = re.findall(pattern, team)
                    for correspondence in correspondences:
                        num = correspondence
                        ls_max.append(num)
                        #print(ls_max)
            max_num = max(ls_max)
            max_num = int(max_num)
            try:
                if not self.dicto_team_real[y]:
                    pass
                else:
                    for team in self.dicto_team_real[y]:
                        pattern = r'\d+\.\d+|\d+'
                        team = str(team)
                        correspondences = re.findall(pattern, team)
                        for correspondence in correspondences:
                            num = correspondence
                            ls_max_1.append(num)
                max_num_y = max(ls_max_1)
                print(max_num_y)
                max_num_y = int(max_num_y)
                print(max_num_y)
            except KeyError:
                pass
            
        
        
        #print(max_num_y)
        x = x + max_num_y +1
        #print(x)
        
        for i in range(max_num_y, x):
            self.dicto_team_real.setdefault(y, []).append([i, col, f"team{i+1}"])
        self.value_automat.emit(self.dicto_team_real)


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
