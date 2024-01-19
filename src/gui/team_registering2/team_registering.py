from PySide6 import QtCore, QtWidgets, QtGui
import sys
import math

from tab.first_tab import FirstTab
from tab.second_tab import SecondTab
from tab.third_tab import ThirdTab
from dialog.save_teams import SaveTeams
from dialog.settings_combo import SettingCombo

class TeamRegistering(QtWidgets.QWidget):
    header_finder = QtCore.Signal(int)
    opened = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team registering")
        self.team = []
        self.index = [0,0]
        self.row_index = 0
        self.col_index = 0

        self.first_tab = FirstTab()
        self.second_tab = SecondTab()
        self.third_tab = ThirdTab()
        tab_widget = QtWidgets.QTabWidget()
        tab_widget.addTab(self.first_tab, "manuel")
        tab_widget.addTab(self.second_tab, "générer")

        self.first_tab.value.connect(self.fill)

        pushbutton_3 = QtWidgets.QPushButton("Annuler")
        pushbutton_4 = QtWidgets.QPushButton("Suivant")
        pushbutton_5 = QtWidgets.QPushButton("Ajouter des joueurs")
        self.table = QtWidgets.QTableWidget()

        self.table.installEventFilter(self)
        self.table.setColumnCount(3)

        self.resizeEvent = self.adjust_columns

        layout_base = QtWidgets.QVBoxLayout(self)
        layout_button = QtWidgets.QHBoxLayout()
        layout_middle = QtWidgets.QHBoxLayout()
        layout_table = QtWidgets.QVBoxLayout()

        layout_button.addWidget(pushbutton_3)
        layout_button.addWidget(pushbutton_4)
        layout_table.addWidget(pushbutton_5)
        layout_table.addWidget(self.table)
        layout_middle.addWidget(tab_widget)
        layout_middle.addLayout(layout_table)
        layout_base.addLayout(layout_middle)
        layout_base.addLayout(layout_button)

        pushbutton_3.clicked.connect(self.open_back)
        self.table.cellClicked.connect(self.second_event )
    
    def open_back(self):
        self.opened.emit()
        self.close()
    
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if source is self.table and event.type() == QtCore.QEvent.KeyPress:
            key_event = event
            key = key_event.key()
            if key == QtCore.Qt.Key_Delete:
                selected_items = self.table.selectedItems()
                if selected_items and self.table.currentColumn()!=0:
                    #selected_value = selected_items[0].text()
                    #print(f"Touche 'u' enfoncée avec la cellule sélectionnée : {selected_value}")
                    self.index = [self.table.currentRow(), self.table.currentColumn()-1]
                    self.col_index = self.table.currentColumn()
                    self.row_index = self.table.currentRow()
                    '''if len(selected_items)==3:
                        self.table.setItem(self.row_index, 0, QtWidgets.QTableWidgetItem(""))'''
                    for item in selected_items:
                        item_text = item.text()
                        for row in self.team:
                            for i in row:
                                if i == item_text:
                                    self.table.setItem(self.row_index, row.index(i)+1, QtWidgets.QTableWidgetItem(""))

                    if len(selected_items) == 3:
                        self.table.setItem(self.row_index, 0, QtWidgets.QTableWidgetItem(""))


        return super().eventFilter(source, event)

    def second_event(self):
        selected_items = self.table.selectedItems()
        if selected_items and self.table.currentColumn()!=0:
            #selected_value = selected_items[0].text()
            ##print(f"Touche 'u' enfoncée avec la cellule sélectionnée : {selected_value}")
            self.index = [self.table.currentRow(), self.table.currentColumn()-1]
            self.col_index = self.table.currentColumn()-1
            self.row_index = self.table.currentRow()
            #print('##### CHANGE #####')
                
    @QtCore.Slot(str)
    def fill(self, str):
        #init
        self.team.append([])
        if self.row_index+1>self.table.rowCount():
            self.table.setRowCount(self.row_index+1)
        #print(self.row_index, self.col_index)
        #verif
        if self.team[self.row_index]==[] or len(self.team[self.row_index])==1:
            self.team[self.row_index].append(str)
            #print('1')
        else:
            self.team[self.row_index][self.col_index]=str
            #print('2')

        #set in table
        self.table.setItem(self.row_index, self.col_index+1, QtWidgets.QTableWidgetItem(str))
        self.table.setCurrentCell(self.row_index, self.col_index+1)

        #end
        if self.col_index==1:
            #print('4')
            self.table.setItem(self.row_index, 0, QtWidgets.QTableWidgetItem(f"{self.team[self.row_index][self.col_index-1]}_{self.team[self.row_index][self.col_index]}"))
            self.row_index= self.row_index+1
        if self.col_index==0:
            #print("3")
            self.col_index=1
        else:
            self.col_index=0
        
        #print('-----------------------------')
    
    def adjust_columns(self, event):
        window_width = self.table.size().width()
        column_width = window_width / 3
        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, column_width)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TeamRegistering()

    widget.resize(800, 500)
    widget.show()

    sys.exit(app.exec())