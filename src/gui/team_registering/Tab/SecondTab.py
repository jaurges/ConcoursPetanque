from PySide6 import QtWidgets, QtGui, QtCore

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