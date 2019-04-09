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
        self.pte_api_key = QtWidgets.QPlainTextEdit(Dialog)
        self.pte_api_key.setGeometry(QtCore.QRect(10, 20, 600, 31))
        self.pte_api_key.setMinimumSize(QtCore.QSize(600, 31))
        self.pte_api_key.setMaximumSize(QtCore.QSize(600, 31))
        self.pte_api_key.setTabChangesFocus(True)
        self.pte_api_key.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.pte_api_key.setObjectName("pte_api_key")
        self.btn_bx_api_key = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_bx_api_key.setGeometry(QtCore.QRect(60, 80, 186, 32))
        self.btn_bx_api_key.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_bx_api_key.setObjectName("btn_bx_api_key")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "API Key"))
        self.pte_api_key.setPlainText(_translate("Dialog", "Enter an API key here ..."))


