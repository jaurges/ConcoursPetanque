from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QEvent, QObject

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)

        for i in range(5):
            for j in range(5):
                item = QTableWidgetItem(f'Row {i}, Col {j}')
                self.tableWidget.setItem(i, j, item)

        layout = QVBoxLayout(self)
        layout.addWidget(self.tableWidget)

        # Connecter la fonction eventFilter à l'événement clavier
        self.tableWidget.installEventFilter(self)

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if source is self.tableWidget and event.type() == QEvent.KeyPress:
            key_event = event
            key = key_event.key()
            if key == Qt.Key_U:
                # Vérifier si une cellule est sélectionnée
                selected_items = self.tableWidget.selectedItems()
                if selected_items:
                    # Récupérer la valeur de la cellule sélectionnée
                    selected_value = selected_items[0].text()
                    print(f"Touche 'u' enfoncée avec la cellule sélectionnée : {selected_value}")

        return super().eventFilter(source, event)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
