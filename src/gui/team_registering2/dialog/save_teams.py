import sys
import random
import csv
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from src.application import Application


class SaveTeams(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 200)

        label1 = QtWidgets.QLabel("Enregister dans un tableur :")
        label2 = QtWidgets.QLabel("Enregister dans un fichier texte brut :")
        label3 = QtWidgets.QLabel("Enregistrer dans la base de donnée : (recommandée)")

        button1 = QtWidgets.QToolButton()
        button2 = QtWidgets.QToolButton()
        button3 = QtWidgets.QToolButton()
        button1.setIcon(QtGui.QIcon("images/table.svg"))
        button2.setIcon(QtGui.QIcon("images/align-left.svg"))
        button3.setIcon(QtGui.QIcon("images/database.svg"))

        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        layout3 = QtWidgets.QHBoxLayout()
        layout_base = QtWidgets.QVBoxLayout(self)

        layout1.addWidget(label1)
        layout1.addWidget(button1)
        layout2.addWidget(label2)
        layout2.addWidget(button2)
        layout3.addWidget(label3)
        layout3.addWidget(button3)
        layout_base.addLayout(layout1)
        layout_base.addLayout(layout2)
        layout_base.addLayout(layout3)

        button1.clicked.connect(self.save_csv)
        button2.clicked.connect(self.save_txt)
    
    def save_txt(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.ReadOnly
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setOptions(options)

        file_name = file_dialog.getSaveFileName(self, "Enregistrer un fichier", "", "Fichiers texte (*.txt)")


        try: 
            if file_name:
                with open(file_name, 'w') as file:
                    file.write("le tout des équipes")
        except TypeError:
            pass
    
    def save_csv(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.ReadOnly
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setOptions(options)

        file_name, _ = file_dialog.getSaveFileName(self, "Enregistrer un fichier", "", "Tableur (*.csv)")

        if file_name:
            with open(f"{file_name}.csv", mode='w', newline='') as fichier:
                writer = csv.writer(fichier)

                for row in range(5):
                    if row == 4: 
                        ligne_a_inserer = [""] * 5
                        ligne_a_inserer[2] = str(random.randint(1, 100))
                        writer.writerow(ligne_a_inserer)
                    else:
                        writer.writerow([""] * 5)