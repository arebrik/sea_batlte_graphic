from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class MyGScene(QGraphicsScene):

    pos_img = 'resource/pos.png'
    ship1_img = 'resource/ship1.png'
    ship2_img = 'resource/ship2.png'
    ship3_img = 'resource/ship3.png'
    boom_img = 'resource/boom.png'

    selected_item = pyqtSignal(list, name='selected_item')

    def __init__(self, transform):
        super().__init__()
        self.setSceneRect(0, 0, 0, 0)
        self.transform = transform
        self.ships = []

    def draw_start_my_field(self, ships):
        self._tmp_ships = ships
        self.points = {}
        x_pos = -200
        y_pos = -50
        for y in range(10):
            for x in range(10):
                self.points[(x, y)] = self.addPixmap(QPixmap(self.pos_img))
                self.points[(x, y)].setPos(x_pos, y_pos)
                self.points[(x, y)].coordinate = x, y
                ship = self.check_ship((x,y))
                if ship:
                    self.points[(x,y)].setVisible(False)
                    self.draw_ship(ship, (x,y), x_pos, y_pos)
                x_pos += 50
            x_pos = -200
            y_pos += 50

    def check_ship(self, coordinate:tuple):
        for ship in self._tmp_ships:
            if coordinate in ship.coordinate:
                return ship
        return False

    def draw_ship(self, ship, coordinate:tuple, x_pos:int, y_pos:int):
        if ship.coordinate[0] == coordinate:
            if ship.horizontal == 0:
                self.ships.append(self.addPixmap(
                        QPixmap('resource/ship{}{}'.format(ship.ship_len, '')))
                )
            else:
                self.ships.append(self.addPixmap(
                    QPixmap('resource/ship{}{}'.format(ship.ship_len, '_v')))
                )
            self.ships[-1].coordinate = ship.coordinate
            self.ships[-1].c_history = ship.coordinate[:]
            self.ships[-1].ship_len = ship.ship_len
            self.ships[-1].setPos(x_pos, y_pos)

    def redraw_field(self, point, answer):
        if answer == 'mimo':
            self.points[point].setVisible(False)
        else:
            boom = self.addPixmap(QPixmap(self.boom_img))
            boom.setPos(self.points[point].pos())
            if answer.find('kill') != -1:
                coordinates = answer[answer.rfind('l') + 1:len(answer)].split(';')
                coordinates = [(int(z[0]), int(z[2])) for z in coordinates]
                self.redraw_field_kill(coordinates)

    def redraw_field_kill(self, coordinates):
        for c in coordinates:
            for point in self.points:
                if ((abs(c[0] - point[0]) == 1 and abs(c[1] - point[1]) < 2)
                    or (abs(c[1] - point[1]) == 1 and abs(c[0] - point[0]) < 2)):
                    self.points[point].setVisible(False)
