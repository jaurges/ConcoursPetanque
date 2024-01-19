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
                        for row in self.team:
                            for i in row:
                                if i == item.text():
                                    self.table.setItem(self.row_index, row.index(i)+1, QtWidgets.QTableWidgetItem("caca"))

        return super().eventFilter(source, event)