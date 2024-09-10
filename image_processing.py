from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QPainter

class GraphicsView(QGraphicsView):
    pointsSignal = pyqtSignal(str)
    pointsSignal2 = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setTransformationAnchor(self.AnchorUnderMouse)
        self.setRenderHints(QPainter.Antialiasing |
                            QPainter.HighQualityAntialiasing |
                            QPainter.TextAntialiasing |
                            QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setDragMode(self.RubberBandDrag)
        self.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.itemsToShapes = {}
        self.shapesToItems = {}
        self.Rectmode = True
        self.bboxPointList = []
        self.labelList = []
        self.bboxList = []

    def show_image(self, image_path):
        self.scene.clear()
        image = QPixmap(image_path)
        scaled_image = image.scaled(self.height(), self.height(), Qt.IgnoreAspectRatio)
        self.image_item = QGraphicsPixmapItem(scaled_image)
        self.scene.addItem(self.image_item)

    # Additional methods for handling graphics view operations
