from .ui.Ui_main_field import Ui_MainField
from PyQt5.QtWidgets import QWidget, QMessageBox
from .EnemyGScene import EnemyGScene
from .MyGScene import MyGScene
from core.NetAPI import NetInterface
import sys

class MainFiled(QWidget, Ui_MainField):

    ip = ''
    is_server = None
    is_turn = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
        self.interface = NetInterface()
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
        self.interface.is_get.connect(self.enemy_turn)

    def selected_enemy(self, item:tuple):
        if self.is_turn:
            item_f = str(item[0]) + ',' + str(item[1])
            self.interface.send(item_f)
            answer = self.interface.get()
            if answer == 'terminate connection':
                self.interface.send_finish()
                QMessageBox.information(self, 'Игра окончена', 'Ты победил!!!')
                sys.exit()
            elif answer == 'mimo':
                self.is_turn = False
                self.is_turn_lbl.setText('Ход противника!')
            self.eneme_scene.redraw_field(item, answer)

    def enemy_turn(self):
        answer = self.interface.get()
        if answer == 'terminate connection':
            QMessageBox.information(self, 'Игра окончена', 'Ты проиграл!!!')
            sys.exit()
        answer = int(answer[0]), int(answer[2])
        result = self.check_point(answer)
        self.interface.send(result)
        if result == 'mimo':
            self.is_turn = True
            self.is_turn_lbl.setText('Твой ход!')

    def check_point(self, point):
        for i, ship in enumerate(self.my_scene.ships):
            if point in ship.coordinate:
                self.my_scene.ships[i].coordinate.pop(self.my_scene.ships[i].coordinate.index(point))
                if self.my_scene.ships[i].coordinate:
                    self.my_scene.redraw_field(point, 'popal')
                    return 'popal'
                else:
                    if self.check_finish():
                        QMessageBox.information(self, 'Игра окончена', 'Ты проиграл!!!')
                        sys.exit()
                    full_coordinate = ship.c_history
                    full_coordinate_str = ';'.join([','.join([str(i)
                                                        for i in full_coordinate[y]])
                                                            for y in range(len(full_coordinate))])
                    self.my_scene.redraw_field(point, 'kill' + full_coordinate_str)
                    return 'kill' + full_coordinate_str
        self.my_scene.redraw_field(point, 'mimo')
        return 'mimo'

    def check_finish(self):
        for ship in self.my_scene.ships:
            if ship.coordinate:
                break
        else:
            self.interface.send_finish()
            return True

    def push_ships(self, ships):
        self.my_scene.draw_start_my_field(ships)

    def main(self):
        if not self.is_server:
            self.interface.ip = self.ip
            self.is_turn = True
            self.is_turn_lbl.setText('Твой ход!')
        else:
            self.is_turn_lbl.setText('Ход противника!')
        self.interface.start_listen()

        if self.is_server:
            self.interface.get_test_connect()
            self.interface.send(self.my_name_lbl.text())
            self.enemy_name_lbl.setText(self.interface.get())
        else:
            self.interface.test_connect()
            enemy_name = self.interface.get()
            self.enemy_name_lbl.setText(enemy_name)
            self.interface.send(self.my_name_lbl.text())

