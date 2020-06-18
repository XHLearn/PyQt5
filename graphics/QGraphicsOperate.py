# -*- coding:utf-8 -*-
'''
@Description: 操作
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-04-17 11:09:34
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QLineF, QPointF, QRectF, Qt
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QTransform
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsScene, QGraphicsView


class CView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(CView, self).__init__(parent)
        self.m_Scene = CScene(self)
        self.m_Scale = 1.0
        self.m_zoomDelta = 0.1
        self.m_translateSpeed = 1.0
        self.m_bMouseTranslate = False
        self.m_lastMousePos = None
        self._InitUI()

    def _InitUI(self):
        INT_MIN = 2000
        INT_MAX = 1000
        self.setScene(self.m_Scene)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCursor(Qt.PointingHandCursor)
        self.setRenderHint(QPainter.Antialiasing)
        self.setSceneRect(INT_MIN/2, INT_MIN/2, INT_MAX, INT_MAX)
        self.centerOn(0, 0)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.m_bMouseTranslate = True
            self.m_lastMousePos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        if self.m_bMouseTranslate:
            offPos = self.mapToScene(pos) - self.mapToScene(self.m_lastMousePos)
            # self.translate(offPos.x(), offPos.y())
            self.translate(offPos)
        self.m_lastMousePos = pos
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            self.m_bMouseTranslate = False
        super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        scrollAmount = event.angleDelta()
        if scrollAmount.y() > 0:
            self.zoom(1+self.m_zoomDelta)
        else:
            self.zoom(1-self.m_zoomDelta)

    def ViewWidth(self):
        self.viewport().rect().width()

    def ViewHeight(self):
        self.viewport().rect().height()

    def zoom(self, scaleF):
        factor = self.transform().scale(scaleF, scaleF).mapRect(QRectF(0, 0, 1, 1)).width()
        if factor < 0.07 or factor > 100:
            return
        self.scale(scaleF, scaleF)
        self.m_Scale *= scaleF

    def translate(self, delta):
        delta *= self.m_Scale
        delta *= self.m_translateSpeed
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        center = QPointF(self.ViewWidth()/2, delta.x(), self.ViewHeight()/2, delta.y())
        self.centerOn(self.mapToScene(center))
        self.setTransformationAnchor(QGraphicsView.AnchorViewCenter)


class CScene(QtWidgets.QGraphicsScene):
    m_LineZValue = -1000
    m_SmallSize = 16
    m_BigSize = 128

    def __init__(self, parent=None):
        super(CScene, self).__init__(parent)
        self._InitUI()

    def _InitUI(self):
        x, y, w, h = -10000, -10000, 20000, 20000
        self.setSceneRect(QRectF(x, y, w, h))
        smallPen = QPen(QColor(64, 64, 64))
        for yTemp in range(x, x+w, self.m_SmallSize):
            self._AddBackLineItem(x, yTemp, x+w, yTemp, smallPen)
        for xTemp in range(y, y+h, self.m_SmallSize):
            self._AddBackLineItem(xTemp, y, xTemp, y+h, smallPen)
        bigPen = QPen(Qt.black)
        for yTemp in range(x, x+w, self.m_BigSize):
            self._AddBackLineItem(x, yTemp, x+w, yTemp, bigPen)
        for xTemp in range(y, y+h, self.m_BigSize):
            self._AddBackLineItem(xTemp, y, xTemp, y+h, bigPen)
        self.setBackgroundBrush(QBrush(QColor(38, 38, 38)))

    def _AddBackLineItem(self, x1, y1, x2, y2, pen):
        line = QGraphicsLineItem(x1, y1, x2, y2)
        line.setPen(pen)
        line.setZValue(self.m_LineZValue)
        self.addItem(line)

    def wheelEvent(self, event):
        super().wheelEvent(event)
        # 吞噬信号，不再将信号返回父窗口，禁止父窗口滑动条操作
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
