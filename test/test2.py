from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6 import QtCore
import sys 

class TableClickDetector(QWidget):
    def __init__(self):
        super(TableClickDetector, self).__init__()

        # Créer un tableau avec quelques données
        self.table = QTableWidget(3, 3, self)
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(f"Cellule {i}-{j}")
                self.table.setItem(i, j, item)

        # Installer l'eventFilter sur le tableau
        self.table.installEventFilter(self)

        # Créer un layout vertical
        layout = QVBoxLayout(self)
        layout.addWidget(self.table)

    def eventFilter(self, obj, event):
        if obj == self.table and event.type() == QtCore.QEvent.MouseButtonPress:
            # Récupérer la position du clic
            pos = event.pos()

            # Récupérer la cellule correspondante
            item = self.table.itemAt(pos)

            if item:
                # Récupérer les indices de ligne et de colonne de la cellule
                row = item.row()
                col = item.column()

                print(f"Clic sur la cellule ({row}, {col})")

        # Appeler le gestionnaire d'événements parent après avoir traité l'événement
        return super().eventFilter(obj, event)

def main():
    app = QApplication([])
    window = TableClickDetector()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
