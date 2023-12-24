import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class TeamRegistering(QtWidgets.QWidget):
    header_finder = QtCore.Signal(int)
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")
        self.team_data = {}
        self.index_club = {}
        self.n = 0

        self.first_tab = FirstTab()
        self.second_tab = SecondTab()
        self.third_tab = ThirdTab()
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.first_tab, "manuel")
        tab_widget.addTab(self.second_tab, "générer")
        tab_widget.addTab(self.third_tab, "importer")

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
        pushbutton_5 = QtWidgets.QPushButton("Enregister")
        #tool_button = QtWidgets.QToolButton()
        self.table = QtWidgets.QTableWidget()

        #tool_button.setIcon(QtGui.QIcon("images/corner-down-left.svg"))

        layout_base = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout_middle = QtWidgets.QHBoxLayout()
        layout_table = QtWidgets.QVBoxLayout()

        #layout_button.addWidget(tool_button)
        layout_button.addWidget(pushbutton_3)
        layout_button.addWidget(pushbutton_4)
        layout_table.addWidget(pushbutton_5)
        layout_table.addWidget(self.table)
        layout_middle.addWidget(tab_widget)
        layout_middle.addLayout(layout_table)
        layout_base.addLayout(layout_middle)
        layout_base.addLayout(layout_button)

        pushbutton_3.clicked.connect(self.open_back)
        pushbutton_5.clicked.connect(self.open_savings)
    
    def open_back(self):
        self.opened.emit()
        self.close()
    
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
        self.table.setRowCount
        for i in dicto:
            for j in dicto[i]:
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
    
    def open_savings(self):
        widget = SaveTeams()
        #widget.resize(360, 100)
        widget.exec()


class SaveTeams(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 200)

        label1 = QtWidgets.QLabel("Enregister dans un tableur :")
        label2 = QtWidgets.QLabel("Enregister dans un fichier texte brut :")
        label3 = QtWidgets.QLabel("Enregistrer dans la base de donnée : (recommandée)")

        button1 = QtWidgets.QToolButton()
        button2 = QtWidgets.QToolButton()
        button3 = QtWidgets.QToolButton()
        button1.setIcon(QtGui.QIcon("images/table.svg"))
        button2.setIcon(QtGui.QIcon("images/align-left.svg"))
        button3.setIcon(QtGui.QIcon("images/database.svg"))

        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        layout3 = QtWidgets.QHBoxLayout()
        layout_base = QtWidgets.QVBoxLayout(self)

        layout1.addWidget(label1)
        layout1.addWidget(button1)
        layout2.addWidget(label2)
        layout2.addWidget(button2)
        layout3.addWidget(label3)
        layout3.addWidget(button3)
        layout_base.addLayout(layout1)
        layout_base.addLayout(layout2)
        layout_base.addLayout(layout3)

        button1.clicked.connect(self.save_csv)
        button2.clicked.connect(self.save_txt)
    
    def save_txt(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.ReadOnly
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setOptions(options)

        file_name = file_dialog.getSaveFileName(self, "Enregistrer un fichier", "", "Fichiers texte (*.txt)")


        try: 
            if file_name:
                with open(file_name, 'w') as file:
                    file.write("le tout des équipes")
        except TypeError:
            pass
    
    def save_csv(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.ReadOnly
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setOptions(options)

        file_name, _ = file_dialog.getSaveFileName(self, "Enregistrer un fichier", "", "Tableur (*.csv)")

        if file_name:
            with open(f"{file_name}.csv", mode='w', newline='') as fichier:
                writer = csv.writer(fichier)

                for row in range(5):
                    if row == 4: 
                        ligne_a_inserer = [""] * 5
                        ligne_a_inserer[2] = str(random.randint(1, 100))
                        writer.writerow(ligne_a_inserer)
                    else:
                        writer.writerow([""] * 5)

class SvDatabase(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        

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
        self.ls_row_club = {}
        self.dicto_team_real = {}
        self.dicto_team_num = {}
        self.j = 0
        self.is_deleted = 0
        self.index_club = {}

        self.new_dicto = {}
        self.temp_dict = {}


    @QtCore.Slot()
    def col_count(self):
        value = self.spinbox1.value()
        self.column.emit(value)
    
    @QtCore.Slot()
    def row_count(self):
        value = self.spinbox2.value()
        self.ls_row.append(value)
        x = self.lineEdit.text()
        if self.ls_row_club == {}:
            self.ls_row_club.setdefault(x, []).append(0)
        self.ls_row_club.setdefault(x, []).append(value)
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
        z = 0
        self.new_dicto[y] = x

        print(self.new_dicto[y])
        if y in self.temp_dict:
            del self.temp_dict[y]
        else: 
            pass
        for n in range(self.new_dicto[y]):
            self.temp_dict.setdefault(y, []).append([n, col, f"{y}_{n+1}"])
        print(self.temp_dict)
        self.row.emit(0)
        self.row_count()
        self.value_automat.emit(self.temp_dict)


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
        button_2.clicked.connect(self.close)

    @QtCore.Slot()
    def btn(self):
        self.club.emit(self.lineEdit.text())
        self.lineEdit.clear()
        print("prout")
    
    def close(self):    
        self.hide()

class ThirdTab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QtWidgets.QLabel("Depuis la base de donnée :")
        self.label2 = QtWidgets.QLabel("Depuis un fichier .csv ou .txt :")
        self.button1 = QtWidgets.QPushButton("ouvrir")
        self.button2 = QtWidgets.QPushButton("ouvrir")

        spacer1 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layout_base = QtWidgets.QVBoxLayout(self)
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout2 = QtWidgets.QVBoxLayout()

        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.button1)
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.button2)
        self.layout_base.addSpacerItem(spacer1)
        self.layout_base.addLayout(self.layout1)
        self.layout_base.addSpacerItem(spacer2)
        self.layout_base.addLayout(self.layout2)
        self.layout_base.addSpacerItem(spacer3)

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
