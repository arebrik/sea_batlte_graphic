from .ui.Ui_main_field import Ui_MainField
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem
from .EnemyGScene import EnemyGScene
from .MyGScene import MyGScene
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from core.NetAPI import NetInterface
import sys

class MainFiled(QWidget, Ui_MainField):

    ip = ''
    is_server = None
    is_turn = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)
        self.eneme_scene = EnemyGScene(self.EnemyGView.transform())
        self.EnemyGView.setScene(self.eneme_scene)
        self.EnemyGView.setStyleSheet('background: transparent; border: transparent; border-width: 0px; border-style: solid')
        self.my_scene = MyGScene(self.MyGView.transform())
        self.MyGView.setScene(self.my_scene)
        self.MyGView.setStyleSheet('background: transparent; border: transparent; border-width: 0px; border-style: solid')

    def init_signals(self):
        self.eneme_scene.selected_item.connect(self.selected_enemy)

    def selected_enemy(self, item:tuple):
        if self.is_turn:
            item_f = str(item[0]) + ',' + str(item[1])
            print('Стреляем в ', item)
            self.interface.send(item_f)
            answer = self.interface.get()
            print('Результат', answer)
            if answer == 'terminate connection':
                self.interface.send_finish()
                print('you win!!!')
                sys.exit()
            self.eneme_scene.redraw_field(item, answer)
            self.is_turn = False
            self.label.setText('Not your turn!')
        else:
            answer = self.interface.get()
            answer = int(answer[0]), int(answer[2])
            self.interface.send(self.check_point(answer))
            self.is_turn = True
            self.label.setText('Your turn!!!')

    def check_point(self, point):
        for i, ship in enumerate(self.my_scene.ships):
            if point in ship.coordinate:
                self.my_scene.redraw_field(point, 'popal') #not ready!!!
                self.my_scene.ships[i].coordinate.pop(self.my_scene.ships[i].coordinate.index(point))
                self.check_finish()
                return 'popal'
        self.my_scene.redraw_field(point, 'mimo')
        return 'mimo'

    def check_finish(self):
        for ship in self.my_scene.ships:
            if ship.coordinate:
                break
        else:
            self.interface.send_finish()
            print('U loose!')
            sys.exit()

    def push_ships(self, ships):
        self.my_scene.draw_start_my_field(ships)

    def main(self):
        self.interface = NetInterface()
        if not self.is_server:
            self.interface.ip = self.ip
            self.is_turn = True
            self.label.setText('Your turn!!!')
        else:
            self.label.setText('Not your turn!')
        self.interface.start_listen()

        if self.is_server:
            self.interface.get_test_connect()
            self.interface.send('success connect')
        else:
            self.interface.test_connect()
            print(self.interface.get())

