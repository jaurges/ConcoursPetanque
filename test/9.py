from PySide6 import QtWidgets, QtGui, QtCore

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()

button = QtWidgets.QToolButton()
icon_path = "/home/antonin/Téléchargements/activity.svg"  # Remplacez par le chemin correct de votre icône
icon = QtGui.QIcon(icon_path)

button.setIcon(icon)
#button.setIconSize(QtCore.QSize(50, 50))  # Redimensionne l'icône à 24x24 pixels

layout.addWidget(button)
window.setLayout(layout)

window.show()
app.exec()
