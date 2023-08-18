from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Qt

app = QApplication([])

# Création d'une fenêtre
window = QWidget()
window.setWindowTitle("Exemple de Style Sheet")
window.setGeometry(300, 300, 300, 200)

# Création d'un bouton
button = QPushButton("Cliquez-moi", window)
button.setGeometry(50, 50, 200, 100)

# Définition du style sheet du bouton
button.setStyleSheet(
    """
    QPushButton {
        background-color: blue;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }

    QPushButton:hover {
        background-color: lightblue;
    }
    """
)

# Affichage de la fenêtre
window.show()

# Lancement de l'application
app.exec()