import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Ajouter des équipes et des clubs")

        # Créer des widgets
        self.team_input = QLineEdit()
        self.club_input = QLineEdit()
        self.add_button = QPushButton("Ajouter")
        self.table_widget = QTableWidget()

        # Créer des layouts
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.team_input)
        input_layout.addWidget(self.club_input)
        input_layout.addWidget(self.add_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        # Associer le signal du bouton à la fonction d'ajout
        self.add_button.clicked.connect(self.add_data)

        # Dictionnaire pour stocker les données par club
        self.club_data = {}

    def add_data(self):
        team = self.team_input.text()
        club = self.club_input.text()

        if team and club:
            if club not in self.club_data:
                # Si le club n'existe pas dans le dictionnaire, créez une nouvelle colonne
                column_count = self.table_widget.columnCount()
                self.table_widget.setColumnCount(column_count + 1)
                self.table_widget.setHorizontalHeaderItem(column_count, QTableWidgetItem(club))
                self.club_data[club] = []

            # Ajouter l'équipe au club correspondant
            self.club_data[club].append(team)
            row_position = len(self.club_data[club]) - 1
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, self.table_widget.columnCount() - 1, QTableWidgetItem(team))

            # Effacer les champs de saisie
            self.team_input.clear()
            self.club_input.clear()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
