from PySide6 import QtWidgets
import sys

from gui.welcome_gui import WelcomeGui
from gui.parameters_gui import ParametersGui
from gui.team_registering_gui import Team_registering
from gui.draw_gui import Draw_gui
from gui.team_gui import Team_gui


class Gui:
    def __init__(self):
        self.app = QtWidgets.QApplication([])

        self.welcome = WelcomeGui()
        self.welcome.resize(360, 480)

        self.parameters = ParametersGui()
        self.parameters.resize(360, 480)

        self.registering = Team_registering()
        self.registering.resize(360, 480)

    def show(self, windows):
        windows.show()
        sys.exit(self.app.exec())

'''
class Signal:
    #def __init__(self):
        #super().__init__(self)
    def clicked_button(self):
'''
def signal(windows, button_name):
    pass



#gui = Gui()
#gui.show_welcome()
#welcome = WelcomeGui()
#parameters = gui.show_parameters()
#welcome.button.clicked.connect(parameters)