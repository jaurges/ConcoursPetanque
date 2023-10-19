from PySide6 import QtWidgets
from src.gui.welcome_gui import WelcomeGui
from src.gui.parameters_gui import ParametersGui
from src.gui.team_gui import Team_gui
from src.gui.team_registering_gui import TeamRegistering

app = QtWidgets.QApplication([])

welcome_widget = WelcomeGui()
parameters_widget = ParametersGui()
team_widget = Team_gui()
team_registering_widget = TeamRegistering()

welcome_widget.resize(360, 480)
parameters_widget.resize(360, 480)

welcome_widget.opened.connect(parameters_widget.show)
parameters_widget.opened.connect(team_widget.show)
team_widget.opened.connect(team_registering_widget.show)

parameters_widget.parent_widget = welcome_widget
team_widget.parent_widget = parameters_widget

welcome_widget.show()
app.exec()
