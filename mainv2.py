from PySide6 import QtWidgets
from Python.ConcoursPetanque.team_registering_gui import TeamRegistering, FirstTab, SecondTab

app = QtWidgets.QApplication([])

main_widget = TeamRegistering()
tab1_widget = FirstTab()
tab1_widget.value_added.connect(main_widget.value_added_func)

main_widget.show()
app.exec()