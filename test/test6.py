from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QComboBox, QVBoxLayout, QWidget
import sys
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)  # Une seule rangée

        # Créer des QComboBox et les ajouter à la première rangée
        for col in range(self.tableWidget.columnCount()):
            combo_box = QComboBox()
            combo_box.addItem("Option 1")
            combo_box.addItem("Option 2")
            combo_box.addItem("Option 3")

            # Connecter le signal currentIndexChanged au callback
            combo_box.currentIndexChanged.connect(self.handleComboBoxChange)

            item = QTableWidgetItem()
            self.tableWidget.setItem(0, col, item)
            self.tableWidget.setCellWidget(0, col, combo_box)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def handleComboBoxChange(self, index):
        sender = self.sender()  # Obtenir l'objet qui a émis le signal
        selected_text = sender.currentText()
        column_index = self.tableWidget.indexAt(sender.pos()).column()

        print(f"ComboBox in column {column_index} changed. New selection: {selected_text}")

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

