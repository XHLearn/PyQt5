# -*- coding:utf-8 -*-
'''
@Description: 在线程操作视图，需要用到QtCore.pyqtSignal信号传递
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-04-01 16:11:55
'''

import sys
import weakref
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QGraphicsItem
from PyQt5.QtCore import QLineF, QPointF, QRectF
from PyQt5.QtGui import QBrush, QColor, QPen, QPolygonF

g_Signal = None


def GetSignal():
    global g_Signal
    if not g_Signal:
        g_Signal = CSignalMgr()
    return g_Signal


class CView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(CView, self).__init__(parent)
        self.m_Scene = CScene(self)
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        global g_Scene
        g_Scene = self.m_Scene
        self.setScene(self.m_Scene)

    def _InitSignal(self):
        pass


class CScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(CScene, self).__init__(parent)
        self.m_Item = None
        self._InitUI()
        self._InitSignal()
        self._InitThread()

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

    def _InitThread(self):
        self.m_Thread = CThread()
        self.m_Thread.start()

    def _InitSignal(self):
        GetSignal().SHOW_POLY.connect(self.SetPoly)


class CSignalMgr(QtCore.QObject):
    SHOW_POLY = QtCore.pyqtSignal(object)


class CThread(QtCore.QThread):

    def run(self):
        tt = 200
        lstPos = [
            [0, 0],
            [tt, 0],
            [tt, tt],
            [0, tt],
        ]
        num = 1
        while True:
            t = num % 4
            pos = QPointF(*lstPos[t])
            GetSignal().SHOW_POLY.emit(pos)  # 这里一定需要通过QtCore.pyqtSignal信号传递
            time.sleep(3)
            num += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
