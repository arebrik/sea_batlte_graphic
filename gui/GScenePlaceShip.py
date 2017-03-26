from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPixmap


class GraphicScene(QGraphicsScene):


    ship1_img = 'resource/ship1.png'
    ship2_img = 'resource/ship2.png'
    ship3_img = 'resource/ship3.png'
    pos_img = 'resource/pos.png'

    def __init__(self, transform):
        super().__init__()
        self.transform = transform
        self.tst_draw()
        self.setSceneRect(0, 0, 0, 0)

    def tst_draw(self):
        self.points={}
        x_pos = -200
        y_pos = -50
        for y in range(10):
            for x in range(10):
                self.points[(x,y)] = self.addPixmap(QPixmap(self.pos_img))
                self.points[(x,y)].setPos(x_pos, y_pos)
                self.points[(x,y)].coordinate = x,y
                x_pos += 50
            x_pos = -200
            y_pos += 50

        self.ships = []
        _h = 350
        for i in range(10):
            if i == 5:
                _h = 450
            if i < 4:
                self.ships.append(self.addPixmap(QPixmap('resource/ship{}.png'.format(1))))
                self.ships[-1].pixmap_v = QPixmap('resource/ship{}_v.png'.format(1))
                self.ships[-1].ship_len = 1
            elif i < 7:
                self.ships.append(self.addPixmap(QPixmap('resource/ship{}.png'.format(2))))
                self.ships[-1].pixmap_v = QPixmap('resource/ship{}_v.png'.format(2))
                self.ships[-1].ship_len = 2
            elif i < 9:
                self.ships.append(self.addPixmap(QPixmap('resource/ship{}.png'.format(3))))
                self.ships[-1].pixmap_v = QPixmap('resource/ship{}_v.png'.format(3))
                self.ships[-1].ship_len = 3
            else:
                self.ships.append(self.addPixmap(QPixmap('resource/ship{}.png'.format(4))))
                self.ships[-1].pixmap_v = QPixmap('resource/ship{}_v.png'.format(4))
                self.ships[-1].ship_len = 4
            self.ships[-1].pixmap_h = self.ships[-1].pixmap()
            self.ships[-1].setFlag(True)
            self.ships[-1].coordinate = []
            self.ships[-1].horizontal = 0
            self.ships[-1].setPos(_h, 100 * i if _h == 350 else 100 * (i-5))
            self.ships[-1].my_base_pos = self.ships[-1].pos()

    def hide_neighbors(self, ship):
        for coordinate in ship.coordinate:
            self.points[coordinate].setVisible(False)

    def fill_coordinate(self, ship, start_coordinate):
        gen_coordinate = [ (start_coordinate[0] + i , start_coordinate[1])
                          if ship.horizontal == 0 else
                          (start_coordinate[0], start_coordinate[1] + i)
                          for i in range(ship.ship_len) ]
        if self.check_neighbors(gen_coordinate):
            ship.coordinate = gen_coordinate
            return True
        else:
            return False

    def show_neighbors(self, coordinates):
        for coordinate in coordinates:
            self.points[coordinate].setVisible(True)

    def check_neighbors(self, new_c):
        for ship in self.ships:
            for coordinate in ship.coordinate:
                for c in new_c:
                    if (abs(c[0] - coordinate[0]) > 1
                        or abs(c[1] - coordinate[1]) > 1):
                        pass
                    else:
                        return False
        return True

    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        find_item = self.itemAt(event.scenePos(), self.transform)
        if find_item:
            if hasattr(find_item, 'ship_len'):
                if find_item.coordinate:
                    self.show_neighbors(find_item.coordinate)
                    find_item.coordinate =[]
                    find_item.setPos(300,150)
                if find_item.horizontal == 0:
                    find_item.horizontal = 1
                    find_item.setPixmap(find_item.pixmap_v)
                else:
                    find_item.setPixmap(find_item.pixmap_h)
                    find_item.horizontal = 0

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        items = self.items(event.scenePos())
        if len(items) == 2:
            if items[0] in self.points.values():
                point = 0
                ship = 1
            else:
                point = 1
                ship = 0
            if hasattr(items[point], 'my_base_pos'):
                items[point].setPos(items[point].my_base_pos)
                items[ship].setPos(items[ship].my_base_pos)
            else:
                change_vector = items[ship].horizontal
                if items[point].coordinate[change_vector] + items[ship].ship_len <= 10:
                    if self.fill_coordinate(items[ship], items[point].coordinate):
                        self.hide_neighbors(items[ship])
                        items[ship].setPos(items[point].pos())
                    else:
                        items[ship].setPos(items[ship].my_base_pos)
                else:
                    items[ship].setPos(items[ship].my_base_pos)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        find_item = self.itemAt(event.scenePos(), self.transform)
        if find_item:
            find_item_pos = find_item.pos()
            try:
                ship_len = find_item.ship_len
                if find_item.coordinate:
                    self.show_neighbors(find_item.coordinate)
                    find_item.coordinate = []
            except AttributeError:
                pass
