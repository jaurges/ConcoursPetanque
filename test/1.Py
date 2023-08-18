import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from aifc import Error


def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')

    # try to open the database
    if not db.open():
        raise Error("Could not open the database")

    query = QSqlQuery()

    # create a table
    query.exec_('''create table t1(
      id INTEGER PRIMARY KEY, fruit TEXT, inventory int);''')

    # populate the table
    query.exec_("insert into t1 (fruit, inventory) values('banana', 3);")
    query.exec_("insert into t1 (fruit, inventory) values('mango', 10);")
    query.exec_("insert into t1 (fruit, inventory) values('cherry', 55);")

    db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    createDB()