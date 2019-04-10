#!/home/jessequinn/.pyenv/versions/3.6.8/envs/tagger-3.6.8/bin/python

"""
Unit tests for Tagger.TaggerTV Class.
"""

from unittest import TestCase
import src.main.python.dialogs as dialogs
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtTest import QTest

app = QApplication(sys.argv)

API_KEY = os.path.join(os.path.dirname(__file__), '.api_key')


class UiDialogTests(TestCase):
    def setUp(self):
        self.api_key_dialog = dialogs.Dialog()
        # api_key_dialog.exec_()

    def test_defaults(self):
        """
        Test default Ui Dialog.
        :return:
        """
        self.assertEqual(self.api_key_dialog.le_api_key.text(), 'Enter an API key here ...')

    def test_save_api_key(self):
        """
        Test to save the api_key
        :return:
        """
        self.api_key_dialog.le_api_key.setText('001234567890')
        saveWidget = self.api_key_dialog.btn_bx_api_key.button(self.api_key_dialog.btn_bx_api_key.Save)
        QTest.mouseClick(saveWidget, Qt.LeftButton)
        self.api_key_file = open(API_KEY)
        self.api_key = self.api_key_file.read()
        self.api_key_file.close()
        self.assertEqual(self.api_key, '001234567890')
