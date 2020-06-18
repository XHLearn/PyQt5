# -*- coding:utf-8 -*-
'''
@Description: 样例
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-03-29 15:47:28
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QGraphicsItem
from PyQt5.QtCore import QLineF, QPointF, QRectF
from PyQt5.QtGui import QBrush, QColor, QPen, QPolygonF


class CView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(CView, self).__init__(parent)
        self.m_Scene = CScene(self)
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        self.setScene(self.m_Scene)

    def _InitSignal(self):
        pass


class CScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(CScene, self).__init__(parent)
        self.m_Item = None
        self._InitUI()
        self._InitSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.SetPoly(event.scenePos())

    def _InitUI(self):
        self.setSceneRect(-1000, -1000, 2000, 2000)

    def SetPoly(self, pos: QPointF):
        x, y = pos.x(), pos.y()
        if self.m_Item:
            self.removeItem(self.m_Item)
        poly = QPolygonF()
        poly.clear()
        poly.append(QPointF(x, y))
        poly.append(QPointF(x+100, y))
        poly.append(QPointF(x+200, y-100))
        poly.append(QPointF(x-100, y-100))
        bursh = QBrush(QColor(123, 123, 123, 80))
        pen = QPen(QtCore.Qt.red)
        self.m_Item = self.addPolygon(poly, pen, bursh)

    def _InitSignal(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
