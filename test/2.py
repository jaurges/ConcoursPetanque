import sys
from aifc import Error

from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        # createDB()

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('test.db')

        # try to open the database
        if not self.db.open():
            raise Error("Could not open the database")

        # this will give you the whole table:
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('t1')

        # if you don't need the whole table, you can try
        # using setSort() and setFilter() methods. if
        # those aren't satisfactory for you, you can
        # replace the previous line with:
        #   query = QSqlQuery()
        #   query.exec_('select * from t1')
        #   self.model.setQuery(query)

        self.model.select()

        self.tview = QTableView(self)
        self.tview.setModel(self.model)
        self.tview.resizeColumnsToContents()
        layout = QVBoxLayout()
        layout.addWidget(self.tview)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tv = TableViewer()
    sys.exit(app.exec_())