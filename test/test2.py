from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        # Remplir la table avec des données de test
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Cellule {row}-{col}")
                self.tableWidget.setItem(row, col, item)

        # Écraser une cellule spécifique
        nouvelle_valeur = QTableWidgetItem("Nouvelle valeur")
        self.tableWidget.setItem(1, 1, nouvelle_valeur)

        # Configurer la disposition principale
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        # Configurer le widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    fenetre = MaFenetre()
    fenetre.show()
    app.exec()
