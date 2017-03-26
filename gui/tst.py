from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication

class MyFrame(QGraphicsView):
    def __init__( self, parent = None ):
        super(MyFrame, self).__init__(parent)

        self.setScene(QGraphicsScene())

        # add some items
        x = 0
        y = 0
        w = 45
        h = 45
        pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.green))
        brush = QtGui.QBrush(pen.color().darker(150))

        item = self.scene().addEllipse(x, y, w, h, pen, brush)
        item.setFlag(QGraphicsItem.ItemIsMovable)

if ( __name__ == '__main__' ):
    app = QApplication([])
    f = MyFrame()
    f.show()
    app.exec_()