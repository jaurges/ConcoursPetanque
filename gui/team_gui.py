import sys
sys.path.append(".")
from PySide6 import QtCore, QtWidgets, QtGui
from object.object import Team


class Team_gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team")

        self.listWidget = QtWidgets.QListWidget(self)
        self.label = QtWidgets.QLabel("Affichage des équipes :")

        self.button = QtWidgets.QPushButton("Click me!")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.listWidget)

        self.print_list()

    @QtCore.Slot()
    def print_list(self):
        app = Application()
        output = app.grab_all()
        for row in output:
            row_raw = row[1] + " " + row[2]
            self.listWidget.addItem(row_raw)


class Application:
    def __init__(self):
        self.database_handler = Team("database.db")

    def grab_all(self):
        output = self.database_handler.return_team("team_example")
        return output


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Team_gui()
    widget.resize(360, 480)
    widget.show()

    sys.exit(app.exec())