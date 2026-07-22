from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemple QTableWidget")
        self.setGeometry(100, 100, 400, 300)

        # Créer un QTableWidget
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)  # Définir le nombre de colonnes

        # Ajouter des données exemple
        self.table_widget.setRowCount(5)
        self.table_widget.setItem(0, 0, QTableWidgetItem("John"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Doe"))
        self.table_widget.setItem(0, 2, QTableWidgetItem("30"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("Jane"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Smith"))
        self.table_widget.setItem(1, 2, QTableWidgetItem("25"))

        # Écouter les événements de sélection
        self.table_widget.itemSelectionChanged.connect(self.selection_change)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)

    def selection_change(self):
        selected_items = self.table_widget.selectedItems()

        if len(selected_items) > 0:
            # Obtenir la ligne sélectionnée
            selected_row = selected_items[0].row()

            # Récupérer les valeurs dans la ligne sélectionnée
            values = [self.table_widget.item(selected_row, col).text() for col in range(self.table_widget.columnCount())]

            print("Valeurs de la ligne sélectionnée:", values)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec_())
