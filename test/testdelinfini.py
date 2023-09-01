from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Obtenir l'index d'une colonne par son nom")

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 300, 200)

        # Créer des en-têtes personnalisés pour chaque colonne
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Nom"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Âge"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Ville"))

        # Remplir le tableau avec des données (à titre d'exemple)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Alice"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("30"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("New York"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Bob"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("25"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("Los Angeles"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Carol"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("35"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("Chicago"))

        # Obtenez l'index de la colonne avec le nom "Âge"
        nom_colonne = "Âge"
        index_colonne = self.get_column_index_by_name(nom_colonne)
        print(f"L'index de la colonne '{nom_colonne}' est : {index_colonne}")

    def get_column_index_by_name(self, nom_colonne):
        header = self.tableWidget.horizontalHeaderItem(0)  # Récupérez le premier en-tête de colonne
        for colonne in range(self.tableWidget.columnCount()):
            if header.text() == nom_colonne:
                return colonne
            header = self.tableWidget.horizontalHeaderItem(colonne + 1)  # Passez à l'en-tête suivant
        return -1  # Retourne -1 si le nom de la colonne n'est pas trouvé

def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
