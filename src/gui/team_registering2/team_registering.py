from PySide6 import QtCore, QtWidgets, QtGui
import sys

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
        self.index = 0

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
    
    def open_back(self):
        self.opened.emit()
        self.close()
    
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if source is self.table and event.type() == QtCore.QEvent.KeyPress:
            key_event = event
            key = key_event.key()
            if key == QtCore.Qt.Key_Delete:
                selected_items = self.table.selectedItems()
                if selected_items:
                    #selected_value = selected_items[0].text()
                    #print(f"Touche 'u' enfoncée avec la cellule sélectionnée : {selected_value}")
                    self.index = (self.table.currentRow(), self.table.currentColumn()-1)

        return super().eventFilter(source, event)
                
    @QtCore.Slot(str)
    def fill(self, str):
        if self.table.rowCount()>self.index[0]//2+1:
            print('prout')
        else:
            self.table.setRowCount(self.index[0]//2+1)
        if self.index[0] % 2 != 0:
            if len(self.team)<self.index[0]:
                self.team[-1].append(str)
            else : 
                self.team[self.index[0]][self.index[1]] = str
            col_index = 2
        else:
            if len(self.team)<self.index[0]:
                self.team.append([str])
            else : 
                self.team[self.index[0]][self.index[1]] = str
            col_index=1

        self.index= self.index + 1
        print(self.index)

        for i in self.team:
            for j in i:
                if str==j:
                    row_index = self.team.index(i)
        
        print(row_index, col_index)

        self.table.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(j))
        #print(self.team)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TeamRegistering()

    widget.resize(800, 500)
    widget.show()

    sys.exit(app.exec())