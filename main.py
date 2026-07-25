from PySide6 import QtWidgets
from src.gui.welcome_gui import WelcomeGui
from src.gui.new_competition import NewCompetition
#from src.gui.team_gui import Team_gui
from src.gui.team_registering2.team_registering import TeamRegistering
from src.gui.main_window import MainWindow

app = QtWidgets.QApplication([])

welcome_widget = WelcomeGui()
parameters_widget = NewCompetition()
team_registering_widget = TeamRegistering()
main_window = MainWindow()

# taille des widgets
welcome_widget.resize(360, 480)
parameters_widget.resize(360, 480)
team_registering_widget.resize(480, 480)

# connections des signaux
welcome_widget.next_par.connect(parameters_widget.show)
parameters_widget.next_tea_reg.connect(team_registering_widget.show)
parameters_widget.prev_tea_reg.connect(welcome_widget.show)
team_registering_widget.next_main.connect(main_window.show)


welcome_widget.show()
app.exec()
