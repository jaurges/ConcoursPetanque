from PySide6 import QtWidgets
from gui.welcome_gui import WelcomeGui
from gui.parameters_gui import ParametersGui

app = QtWidgets.QApplication([])

welcome_widget = WelcomeGui()
parameters_widget = ParametersGui()
welcome_widget.opened.connect(parameters_widget.show)
parameters_widget.parent_widget = welcome_widget

welcome_widget.show()
app.exec()