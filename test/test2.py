from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Créer un tableau et le remplir avec des données (c'est juste un exemple)
        self.table = QTableWidget(self)
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.table.setItem(row, col, item)

        # Créer un layout vertical
        layout = QVBoxLayout()

        # Ajouter le tableau au layout
        layout.addWidget(self.table)

        # Créer un widget central et définir le layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # Définir le widget central de la fenêtre
        self.setCentralWidget(central_widget)

        # Définir le titre de la fenêtre et les dimensions
        self.setWindowTitle("Tableau qui s'ajuste à la fenêtre")
        self.setGeometry(100, 100, 600, 400)

        # Connecter le signal resizeEvent à la fonction qui ajuste la taille des colonnes
        self.resizeEvent = self.adjust_columns

    def adjust_columns(self, event):
        # Récupérer la largeur de la fenêtre
        window_width = event.size().width()

        # Calculer la largeur de chaque colonne (par exemple, en divisant la largeur par le nombre de colonnes)
        column_width = window_width / self.table.columnCount()

        # Ajuster la largeur de chaque colonne
        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, column_width)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
