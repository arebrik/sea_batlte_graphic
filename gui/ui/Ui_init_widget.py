# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_init_widget(object):
    def setupUi(self, init_widget):
        init_widget.setObjectName("init_widget")
        init_widget.resize(228, 165)
        init_widget.setMinimumSize(QtCore.QSize(228, 165))
        init_widget.setMaximumSize(QtCore.QSize(228, 165))
        self.verticalLayout = QtWidgets.QVBoxLayout(init_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(init_widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(init_widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.client_name = QtWidgets.QLineEdit(init_widget)
        self.client_name.setObjectName("client_name")
        self.horizontalLayout.addWidget(self.client_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(init_widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.server_button = QtWidgets.QRadioButton(init_widget)
        self.server_button.setText("")
        self.server_button.setObjectName("server_button")
        self.horizontalLayout_2.addWidget(self.server_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(init_widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.client_button = QtWidgets.QRadioButton(init_widget)
        self.client_button.setText("")
        self.client_button.setObjectName("client_button")
        self.horizontalLayout_3.addWidget(self.client_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(init_widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.server_ip = QtWidgets.QLineEdit(init_widget)
        self.server_ip.setObjectName("server_ip")
        self.horizontalLayout_4.addWidget(self.server_ip)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.start_button = QtWidgets.QPushButton(init_widget)
        self.start_button.setEnabled(False)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)

        self.retranslateUi(init_widget)
        QtCore.QMetaObject.connectSlotsByName(init_widget)

    def retranslateUi(self, init_widget):
        _translate = QtCore.QCoreApplication.translate
        init_widget.setWindowTitle(_translate("init_widget", "Form"))
        self.label_5.setText(_translate("init_widget", "                   Prepare for game !"))
        self.label.setText(_translate("init_widget", "Name:"))
        self.label_2.setText(_translate("init_widget", "Server"))
        self.label_3.setText(_translate("init_widget", "Client"))
        self.label_4.setText(_translate("init_widget", "Server IP"))
        self.start_button.setText(_translate("init_widget", "Start!"))

