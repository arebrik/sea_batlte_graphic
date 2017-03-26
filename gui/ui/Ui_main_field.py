# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainField.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainField(object):
    def setupUi(self, MainField):
        MainField.setObjectName("MainField")
        MainField.resize(815, 582)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainField)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.enemy_name_lbl = QtWidgets.QLabel(MainField)
        self.enemy_name_lbl.setObjectName("enemy_name_lbl")
        self.horizontalLayout_2.addWidget(self.enemy_name_lbl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.is_turn_lbl = QtWidgets.QLabel(MainField)
        self.is_turn_lbl.setObjectName("is_turn_lbl")
        self.horizontalLayout_2.addWidget(self.is_turn_lbl)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.my_name_lbl = QtWidgets.QLabel(MainField)
        self.my_name_lbl.setObjectName("my_name_lbl")
        self.horizontalLayout_2.addWidget(self.my_name_lbl)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.EnemyGView = QtWidgets.QGraphicsView(MainField)
        self.EnemyGView.setObjectName("EnemyGView")
        self.horizontalLayout.addWidget(self.EnemyGView)
        self.MyGView = QtWidgets.QGraphicsView(MainField)
        self.MyGView.setObjectName("MyGView")
        self.horizontalLayout.addWidget(self.MyGView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.EnemyGView.raise_()
        self.is_turn_lbl.raise_()

        self.retranslateUi(MainField)
        QtCore.QMetaObject.connectSlotsByName(MainField)

    def retranslateUi(self, MainField):
        _translate = QtCore.QCoreApplication.translate
        MainField.setWindowTitle(_translate("MainField", "Form"))
        self.enemy_name_lbl.setText(_translate("MainField", "Enemy name"))
        self.is_turn_lbl.setText(_translate("MainField", "isTurn"))
        self.my_name_lbl.setText(_translate("MainField", "my name"))

