from .ui.Ui_place_ship_widget import Ui_place_ship_widget
from PyQt5.QtWidgets import QWidget, QMessageBox
from .GScenePlaceShip import GraphicScene
from PyQt5.QtCore import pyqtSignal

class PlaceShip(QWidget, Ui_place_ship_widget):

    finish_place = pyqtSignal(list, name='finish_place')
    ship1_img = 'resource/ship1.png'
    ship2_img = 'resource/ship2.png'
    ship3_img = 'resource/ship3.png'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
        self.init_signals()


    def init_ui(self):
        self.setupUi(self)
        self.scene = GraphicScene(self.ship_base.transform())
        self.ship_base.setScene(self.scene)
        self.ship_base.setStyleSheet('background: transparent; border: transparent; border-width: 0px; border-style: solid')


    def init_signals(self):
        self.start_button.clicked.connect(self.start_clicled)

    def start_clicled(self):
        for ship in self.scene.ships:
            if ship.coordinate == []:
                QMessageBox.critical(self, 'Ошибка расстановки', 'Не раставлены все корабли')
                break
        else:
            self.finish_place.emit(self.scene.ships)