# -*- coding:utf-8 -*-
'''
@Description: wheelevent相关
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-04-01 16:59:03
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QGraphicsItem
from PyQt5.QtCore import QLineF, QRectF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFormLayout, QGroupBox, QHBoxLayout, QLabel, \
    QLineEdit, QVBoxLayout


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

    def wheelEvent(self, event):
        super().wheelEvent(event)
        print("View isAccepted", event.isAccepted())
        print("-"*30)


class CScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(CScene, self).__init__(parent)
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        self.setSceneRect(-1000, -1000, 2000, 2000)
        oItem = CWidget()
        self.addWidget(oItem)

    def _InitSignal(self):
        pass

    def wheelEvent(self, event):
        super().wheelEvent(event)
        # if event.isAccepted():
        #     return
        print("Scene isAccepted", event.isAccepted())
        # event.accept()
        # event.ignore()


class CWidget(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(CWidget, self).__init__(parent)
        self._InitUI()

    def _InitUI(self):
        self.setMaxVisibleItems(10)
        self.setEditable(True)
        for x in range(15):
            self.addItem("Test_" + str(x))

    def wheelEvent(self, event):
        super().wheelEvent(event)
        print("QComboBox isAccepted", event.isAccepted())
        # event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
