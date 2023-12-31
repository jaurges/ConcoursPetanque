from PySide6 import QtWidgets

class MaFenetre(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Autres initialisations de la fenêtre

        # Création d'un bouton pour tester la fermeture de la fenêtre
        self.button = QtWidgets.QPushButton("Fermer la fenêtre", self)
        self.button.clicked.connect(self.fermer_fenetre)

    def fermeture(self):
        # Code à exécuter au moment de la fermeture de la fenêtre
        print("La fenêtre est en train de se fermer")

    def fermer_fenetre(self):
        # Appeler la méthode close() pour déclencher l'événement de fermeture
        self.close()

    def closeEvent(self, event):
        # Redéfinition de la méthode closeEvent pour y ajouter notre comportement personnalisé
        self.fermeture()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    fenetre = MaFenetre()
    fenetre.show()

    app.exec()
