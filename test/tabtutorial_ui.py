# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabtutorial.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1120, 850)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 130, 1121, 721))
        self.tabWidget.setStyleSheet(u"background-color: rgb(253, 255, 242);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1111, 691))
        self.widget.setStyleSheet(u"background-color: rgb(255, 243, 242);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.change = QPushButton(Dialog)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(60, 50, 93, 28))
        self.insert = QPushButton(Dialog)
        self.insert.setObjectName(u"insert")
        self.insert.setGeometry(QRect(220, 50, 93, 28))
        self.remove = QPushButton(Dialog)
        self.remove.setObjectName(u"remove")
        self.remove.setGeometry(QRect(390, 50, 93, 28))

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
        self.change.setText(QCoreApplication.translate("Dialog", u"Change Text", None))
        self.insert.setText(QCoreApplication.translate("Dialog", u"Insert Tab", None))
        self.remove.setText(QCoreApplication.translate("Dialog", u"Remove Tab", None))
    # retranslateUi

