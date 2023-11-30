from PySide6 import QtCore, QtWidgets, QtGui


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