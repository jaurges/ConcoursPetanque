from PySide6 import QtWidgets
from src.gui.welcome_gui import WelcomeGui
from src.gui.parameters_gui import ParametersGui
from src.gui.team_gui import Team_gui

app = QtWidgets.QApplication([])

welcome_widget = WelcomeGui()
parameters_widget = ParametersGui()
team_widget = Team_gui()

welcome_widget.opened.connect(parameters_widget.show)
parameters_widget.opened.connect(team_widget.show)

parameters_widget.parent_widget = welcome_widget
team_widget.parent_widget = parameters_widget

welcome_widget.show()
app.exec()
