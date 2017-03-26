from .ui.Ui_init_widget import Ui_init_widget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class InitWindow(QWidget, Ui_init_widget):

    finish_init = pyqtSignal(tuple, name='finish_init')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

    def init_signals(self):
        self.start_button.clicked.connect(self.on_start_click)
        self.client_name.textChanged.connect(self.check_input)
        self.server_button.toggled.connect(self.check_server)
        self.server_ip.textChanged.connect(self.check_input)

    def on_start_click(self):
        connection_type = self.server_button.isChecked()
        ip = self.server_ip.text()
        self.finish_init.emit((ip, connection_type))

    def check_input(self):
        if self.client_name.text() and self.server_ip.text():
            self.start_button.setEnabled(True)
        else:
            self.start_button.setDisabled(True)

    def check_server(self):
        if self.server_button.isChecked():
            self.server_ip.setText('127.0.0.1')
            self.server_ip.setDisabled(True)
            if self.client_name.text():
                self.start_button.setEnabled(True)
        else:
            self.server_ip.setText('')
            self.server_ip.setEnabled(True)
            self.start_button.setDisabled(True)

