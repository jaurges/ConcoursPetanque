def index_changed(self, index):
    sender = self.sender()
    self.table1.clearContents()  # Efface le contenu actuel de la QTableWidget
    self.table1.setRowCount(len(self.output[sender.currentText()]))

    row_index = 0
    for player in self.output[sender.currentText()]:
        widget = QtWidgets.QWidget()
        checkbox = QtWidgets.QCheckBox()
        label = QtWidgets.QLabel(player)

        layout = QtWidgets.QHBoxLayout(widget)
        layout.addWidget(checkbox)
        layout.addWidget(label)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        widget.setLayout(layout)

        self.table1.setCellWidget(row_index, self.comboboxes.index(sender), widget)

        checkbox.stateChanged.connect(self.checkbox_changed)
        row_index += 1

    self.table2.setHorizontalHeaderItem(self.comboboxes.index(sender), QtWidgets.QTableWidgetItem(sender.currentText()))
