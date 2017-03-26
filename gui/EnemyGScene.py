from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem
from PyQt5.QtCore import QLineF, QPointF, pyqtSignal
from PyQt5.QtGui import QPixmap, QPen, QFont


class EnemyGScene(QGraphicsScene):

    pos_img = 'resource/pos.png'
    boom_img = 'resource/boom.png'

    selected_item = pyqtSignal(tuple, name='selected_item')

    def __init__(self, transform):
        super().__init__()
        self.setSceneRect(0, 0, 0, 0)
        self.transform = transform
        self.draw_enemy_start_points()

    def draw_enemy_start_points(self):
        self.points = {}
        x_pos = -200
        y_pos = -50
        for y in range(10):
            for x in range(10):
                self.points[(x, y)] = self.addPixmap(QPixmap(self.pos_img))
                self.points[(x, y)].setPos(x_pos, y_pos)
                self.points[(x, y)].coordinate = x, y
                x_pos += 50
            x_pos = -200
            y_pos += 50

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        find_item = self.itemAt(event.scenePos(), self.transform)
        if find_item and hasattr(find_item, 'coordinate'):
            self.selected_item.emit(find_item.coordinate)

    def redraw_field(self, coordinate, answer):
        if answer == 'mimo':
            self.points[coordinate].setVisible(False)
        else:
            boom = self.addPixmap(QPixmap(self.boom_img))
            boom.setPos(self.points[coordinate].pos())
            self.points[coordinate].setVisible(False)
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


