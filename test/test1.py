import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Bouton carré avec des coins arrondis")

central_widget = QWidget()
window.setCentralWidget(central_widget)

layout = QVBoxLayout()

# Créez un QPushButton carré avec des coins arrondis
button = QPushButton("Bouton Carré")
button.setFixedSize(100, 100)  # Largeur et hauteur égales pour créer un bouton carré
button.setStyleSheet(
    '''
    QPushButton {
        border: 2px solid #1e90ff; /* Couleur de la bordure */
        border-radius: 10px; /* Rayon des coins arrondis */
        background-color: #f0f0f0; /* Couleur de fond */
        padding: 10px; /* Espace interne */
        font-size: 14px; /* Taille de la police */
    }

    QPushButton:hover {
        background-color: #1e90ff; /* Couleur de fond au survol */
        color: #ffffff; /* Couleur du texte au survol */
    }
    '''
)

layout.addWidget(button)
central_widget.setLayout(layout)

window.show()
sys.exit(app.exec_())
