import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("QTableWidget avec en-têtes personnalisés")

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 300, 200)

        # Créer des en-têtes personnalisés pour chaque colonne
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Colonne 1"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Colonne 2"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Colonne 3"))

        # Remplir le tableau avec des données (à titre d'exemple)
        self.tableWidget.setRowCount(4)
        for row in range(4):
            for col in range(3):
                item = QTableWidgetItem(f"Donnée {row}, {col}")
                self.tableWidget.setItem(row, col, item)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
