import sys
import csv
from PySide6 import QtCore, QtGui, QtWidgets
import random

class SaveTeams(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        label1 = QtWidgets.QLabel("Enregister dans un tableur :")
        label2 = QtWidgets.QLabel("Enregister dans un fichier texte brut :")
        label3 = QtWidgets.QLabel("Enregistrer dans la base de donnée : (recommandée)")

        button1 = QtWidgets.QToolButton()
        button2 = QtWidgets.QToolButton()
        button3 = QtWidgets.QToolButton()
        button1.setIcon(QtGui.QIcon("images/table.svg"))
        button2.setIcon(QtGui.QIcon("images/align-left.svg"))
        button3.setIcon(QtGui.QIcon("images/database.svg"))

        spacer1_1 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer1_2 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        spacer1_3 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer2_1 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer2_2 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        spacer2_3 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer3_1 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        spacer3_2 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        spacer3_3 = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        layout3 = QtWidgets.QHBoxLayout()
        layout_base = QtWidgets.QVBoxLayout(self)

        layout1.addSpacerItem(spacer1_1)
        layout1.addWidget(label1)
        layout1.addSpacerItem(spacer1_2)
        layout1.addWidget(button1)
        layout1.addSpacerItem(spacer1_3)
        layout2.addSpacerItem(spacer2_1)
        layout2.addWidget(label2)
        layout2.addSpacerItem(spacer2_2)
        layout2.addWidget(button2)
        layout2.addSpacerItem(spacer2_3)
        layout3.addSpacerItem(spacer3_1)
        layout3.addWidget(label3)
        layout3.addSpacerItem(spacer3_2)
        layout3.addWidget(button3)
        layout3.addSpacerItem(spacer3_3)
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

        if file_name:
            with open(file_name, 'w') as file:
                file.write("le tout des équipes")
    
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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = SaveTeams()

    widget.resize(500, 100)
    widget.show()

    sys.exit(app.exec())