from PySide6 import QtCore, QtWidgets, QtGui
import sys
import math
sys.path.append(".")
from tab.first_tab import FirstTab
from tab.second_tab import SecondTab
from tab.third_tab import ThirdTab
from dialog.save_teams import SaveTeams
from dialog.settings_combo import SettingCombo

class TeamRegistering(QtWidgets.QWidget):
    header_finder = QtCore.Signal(int)
    next_main = QtCore.Signal()
    previous_param = QtCore.Signal()
    def __init__(self, button : bool = True):
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
        tab_widget.addTab(self.third_tab, "importer")

        self.first_tab.value.connect(self.fill)

        pushbutton_5 = QtWidgets.QPushButton("Ajouter des joueurs")
        self.table = QtWidgets.QTableWidget()

        self.table.installEventFilter(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(("Nom de l'équipe","Joueur 1", "Joueur 2"))
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) # bonne taille des colonnes

        layout_base = QtWidgets.QVBoxLayout(self)
        
        layout_middle = QtWidgets.QHBoxLayout()
        layout_table = QtWidgets.QVBoxLayout()
        layout_table.addWidget(pushbutton_5)
        layout_table.addWidget(self.table)
        layout_middle.addWidget(tab_widget)
        layout_middle.addLayout(layout_table)
        layout_base.addLayout(layout_middle)
        
        self.table.cellClicked.connect(self.second_event )

        layout_button = QtWidgets.QHBoxLayout()
        pushbutton_3 = QtWidgets.QPushButton("Annuler")
        layout_base.addLayout(layout_button)
        layout_button.addWidget(pushbutton_3)
        if button : 
            pushbutton_4 = QtWidgets.QPushButton("Suivant")
            layout_button.addWidget(pushbutton_4)
            pushbutton_3.clicked.connect(self.open_back)
            pushbutton_4.clicked.connect(self.open_next)
        else : 
            pushbutton_6 = QtWidgets.QPushButton("Valider")
            layout_button.addWidget(pushbutton_6)
            pushbutton_3.clicked.connect(self.close)
            pushbutton_6.clicked.connect(self.save_close)
    
    def open_next(self):
        # enregistre le tableau
        self.next_main.emit()
        self.close()

    def open_back(self):
        self.previous_param.emit()
        self.close()

    def save_close(self):
        # enregistre les données et met à jour si besoin
        self.close()

    def save(self):
        #fonctionne pour les deux versions
        output = []
        for row in range(self.table.rowCount()):
            for col in range(3):
                item = self.table.item(row,col)
                output.append(item.text())

    
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool:
        '''sert à effacer une cellule mais attention ne modifie pas les données'''
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
                        try : 
                            item_text = item.text()
                        except RuntimeError:
                            pass
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
            try :
                self.team[self.row_index][self.col_index]=str
            except IndexError:
                print('selectionner une seule case')
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
    
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TeamRegistering()

    widget.resize(800, 500)
    widget.show()

    sys.exit(app.exec())