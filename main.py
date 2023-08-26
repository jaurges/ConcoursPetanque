from PySide6 import QtWidgets
import sys
import threading

from gui.welcome_gui import WelcomeGui as wel
from gui.parameters_gui import ParametersGui as par
from gui.team_registering_gui import Team_registering as team_reg
from gui.draw_gui import Draw_gui as draw
from gui.team_gui import Team_gui as team

app = QtWidgets.QApplication([])
thread = threading.Thread()
thread = threading.

def show_window():
    widget = wel()
    print("1")
    widget.resize(360, 480)
    print("2")
    widget.show()
    print("3")


print("lancement")
show_window()
sys.exit(app.exec())

