# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.setEnabled(True)
        Dialog.resize(623, 124)
        self.btn_bx_api_key = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_bx_api_key.setGeometry(QtCore.QRect(420, 80, 186, 32))
        self.btn_bx_api_key.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_bx_api_key.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.btn_bx_api_key.setObjectName("btn_bx_api_key")
        self.le_api_key = QtWidgets.QLineEdit(Dialog)
        self.le_api_key.setGeometry(QtCore.QRect(10, 20, 600, 31))
        self.le_api_key.setObjectName("le_api_key")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "API Key"))
        self.le_api_key.setText(_translate("Dialog", "Enter an API key here ..."))


