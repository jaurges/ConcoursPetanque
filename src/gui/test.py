import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
sys.path.append(".")
from src.application import Application
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, 
    QVBoxLayout, QTableWidget, QPushButton
)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Gestion de Tournoi - Fenêtre Principale")
        self.resize(900, 600) # Dimensions par défaut pour bien voir les tableaux
        
        self.create_menu_bar()
        
        self.setup_ui()
        self.team_print_in_left_table()

    def create_menu_bar(self):
        """Crée la barre de menu classique type 'Word'"""
        menu_bar = self.menuBar()

        settings_menu = menu_bar.addMenu("Menu")

        config_action = QAction("Modifier les équipes", self)
        config_par = QAction("Modifier les paramètres", self)
        settings_menu.addActions([config_action, config_par])

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)

        self.left_table = QTableWidget(15, 3) 
        
        main_layout.addWidget(self.left_table)

        right_layout = QVBoxLayout()

        self.right_table = QTableWidget(10, 2)
        self.right_table.setHorizontalHeaderLabels(["Classement", "Points"])
        right_layout.addWidget(self.right_table)

        # 2. Le Bouton "Match suivant"
        self.next_match_btn = QPushButton("Match suivant")
        self.next_match_btn.setMinimumHeight(40) # Rend le bouton un peu plus épais, comme sur le dessin
        
        right_layout.addWidget(self.next_match_btn)

        # On ajoute tout ce bloc de droite dans la partie droite du layout principal
        main_layout.addLayout(right_layout)

        # Optionnel : On définit la répartition de l'espace (ici 50% gauche, 50% droite)
        main_layout.setStretch(0, 1) # Colonne gauche
        main_layout.setStretch(1, 1) # Colonne droite

    def team_print_in_left_table(self):
            app = Application()
            n_match = app.get_match_n()
            output = app.return_overall()
            overall = app.overall()
            self.left_table.setRowCount(len(output))
            self.left_table.setColumnCount(n_match+2)
            headers = ['team']
            headers.extend([f"match{i}" for i in range(n_match)])
            headers.append('total')
            headers = tuple(headers)
            self.left_table.setHorizontalHeaderLabels(headers)
            row_index = 0
            for team in overall:
                for row in output:
                    if row[0]==team:
                        self.left_table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row["team"]))
                        self.left_table.setItem(row_index, n_match+1, QtWidgets.QTableWidgetItem(str(row["total"])))
                        for i in range(n_match):
                            self.left_table.setItem(row_index, i+1, QtWidgets.QTableWidgetItem(str(row[f"output{i}"])))
                    else:
                        pass
    
                row_index += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())