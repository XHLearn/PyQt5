# -*- coding:utf-8 -*-
'''
@Description: 样例
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-03-25 16:25:33
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QGraphicsItem
from PyQt5.QtCore import QLineF, QRectF
from PyQt5.QtGui import QColor


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
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        self.setSceneRect(-1000, -1000, 2000, 2000)
        oGroup = CItemGroup()
        self.addItem(oGroup)

    def _InitSignal(self):
        pass


class CItemGroup(QtWidgets.QGraphicsItemGroup):
    def __init__(self, parent=None):
        super(CItemGroup, self).__init__(parent)
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        self.setFiltersChildEvents(False)
        oFrom = QtWidgets.QGraphicsEllipseItem()
        oTo = QtWidgets.QGraphicsRectItem()
        oLine = QtWidgets.QGraphicsLineItem()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        pen = oFrom.pen()
        pen.setWidth(2)
        pen.setColor(QColor(0, 160, 230))
        oFrom.setPen(pen)
        oTo.setPen(pen)
        oLine.setPen(pen)

        oFrom.setBrush(QColor(247, 160, 57))
        oTo.setBrush(QColor(247, 160, 57))

        self.addToGroup(oFrom)
        self.addToGroup(oTo)
        self.addToGroup(oLine)

        length = 50
        oFrom.setRect(QRectF(-length/2, -length/2, length, length))
        oTo.setRect(QRectF(-length/2, -length/2, length, length))

        oFrom.setPos(80, 80)
        oTo.setPos(200, 150)
        oLine.setLine(QLineF(oFrom.pos(), oTo.pos()))

    def _InitSignal(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
