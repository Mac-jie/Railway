from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtCore import Qt

class GraphicsRectItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height, parent=None):
        super().__init__(x, y, width, height, parent)
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        self.setPen(pen)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)

class GraphicItem(QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        pen = QPen(QColor(0, 0, 0, 0))
        pen.setWidth(0.2)
        self.setPen(pen)
        self.setRect(0, 0, 4, 4)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        self.setBrush(Qt.red)

    def hoverLeaveEvent(self, event):
        self.setBrush(Qt.blue)

# Additional custom QGraphicsItem classes
