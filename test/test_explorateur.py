import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Explorateur de fichiers")

        self.button = QPushButton("Ouvrir l'explorateur de fichiers", self)
        self.button.setGeometry(50, 50, 300, 50)
        self.button.clicked.connect(self.openFileDialog)

    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Pour rendre le fichier sélectionné en lecture seule

        filePath, _ = QFileDialog.getOpenFileName(self, "Sélectionnez un fichier", "", "Tous les fichiers (*)", options=options)

        if filePath:
            print(f"Chemin sélectionné : {filePath}")

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
