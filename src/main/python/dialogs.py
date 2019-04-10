import src.main.python.ui as ui
from PyQt5.QtWidgets import QDialog


# API Dialog Class
# TODO: refactor
class Dialog(QDialog, ui.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.btn_bx_api_key.accepted.connect(self.save_api_key)
        self.btn_bx_api_key.rejected.connect(self.reject)

    def save_api_key(self, f='.api_key'):
        try:
            with open(f, 'w') as the_file:
                the_file.write('{0}'.format(self.le_api_key.text()))
        except EnvironmentError:
            # TODO: new error message
            print('error with file write')
            self.reject()
        self.accept()
