# -*- coding:utf-8 -*-
'''
@Description: 样例
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-03-25 20:22:10
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QGraphicsItem
from PyQt5.QtCore import QLineF, QRectF
from PyQt5.QtGui import QColor, QPen


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
        oItem = CRectItem(self)
        self.addItem(oItem)

    def _InitSignal(self):
        pass


class CRectItem(QtWidgets.QGraphicsRectItem):
    def __init__(self, parent=None):
        super(CRectItem, self).__init__()
        self.m_Pos = [0, 0]
        self.m_Size = [400, 200]
        self.m_TextItem = CTextItem()
        self.m_Scene = parent
        self._InitUI()
        self._Resize()

    def _InitUI(self):
        self.setFiltersChildEvents(False)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor(0, 160, 230))
        self.setPen(pen)
        self.setBrush(QColor(247, 160, 57, 20))
        self.m_Scene.addItem(self.m_TextItem)

    def _InitSignal(self):
        pass

    def _Resize(self):
        self.setRect(*(self.m_Pos + self.m_Size))
        self.m_TextItem.Resize(self.m_Pos, self.m_Size)


class CTextItem(QtWidgets.QGraphicsTextItem):
    def __init__(self, parent=None):
        super(CTextItem, self).__init__(parent)
        self._InitUI()

    def _InitUI(self):
        self.setPlainText("QWERTYUIOP")
        self.setBrush(QColor(247, 160, 57, 20))

    def Resize(self, pos, size):
        mysize = [size[0], 20]
        self.setRect(*(pos + mysize))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
