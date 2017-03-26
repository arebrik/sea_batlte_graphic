from .ui.Ui_main_window import Ui_MainWindow
from .InitWindow import InitWindow
from .PlaceShip import PlaceShip
from .MainField import MainFiled
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

        self.init_widget = InitWindow()
        self.place_ship = PlaceShip()
        self.main_field = MainFiled()

        self.stackedWidget.addWidget(self.init_widget)
        self.stackedWidget.addWidget(self.place_ship)
        self.stackedWidget.addWidget(self.main_field)
        self.stackedWidget.setCurrentWidget(self.init_widget)
        self.setMaximumSize(248,205)
        self.setMinimumSize(248,205)


    def init_signals(self):
        self.init_widget.finish_init.connect(self.run_place)
        self.place_ship.finish_place.connect(self.start_main_game)

    def start_main_game(self, ships):
        self.stackedWidget.setCurrentWidget(self.main_field)
        self.main_field.my_name_lbl.setText(self.init_widget.client_name.text())
        self.ships = ships
        self.main_field.push_ships(ships)
        self.main_field.main()
        self.setMaximumSize(1127, 677)
        self.setMinimumSize(1127, 677)

    def run_place(self, ip_info):
        self.main_field.ip = ip_info[0]
        self.main_field.is_server = ip_info[1]
        self.stackedWidget.setCurrentWidget(self.place_ship)
        self.setMaximumSize(900, 750)
        self.setMinimumSize(900, 750)
