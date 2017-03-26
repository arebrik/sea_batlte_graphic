# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'place_ship_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_place_ship_widget(object):
    def setupUi(self, place_ship_widget):
        place_ship_widget.setObjectName("place_ship_widget")
        place_ship_widget.resize(876, 752)
        self.verticalLayout = QtWidgets.QVBoxLayout(place_ship_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(place_ship_widget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 120))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.ship_base = QtWidgets.QGraphicsView(place_ship_widget)
        self.ship_base.setObjectName("ship_base")
        self.verticalLayout.addWidget(self.ship_base)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.start_button = QtWidgets.QPushButton(place_ship_widget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(place_ship_widget)
        QtCore.QMetaObject.connectSlotsByName(place_ship_widget)

    def retranslateUi(self, place_ship_widget):
        _translate = QtCore.QCoreApplication.translate
        place_ship_widget.setWindowTitle(_translate("place_ship_widget", "Form"))
        self.textEdit.setHtml(_translate("place_ship_widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Расстановка кораблей.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Вам необходимо расставить все корабли.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Корабли не могут находиться на соседних клетках, т.е. быть соседями.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Что бы поменять ориентацию корабля, воспользуйтесь двойным щелчком мыши.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Корабль считается установленным, если под ним исчезла клетка моря.</span></p></body></html>"))
        self.start_button.setText(_translate("place_ship_widget", "done"))

