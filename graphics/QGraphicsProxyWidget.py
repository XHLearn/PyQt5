# -*- coding:utf-8 -*-
'''
@Description: 样例
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-03-25 17:09:48
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


class CScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(CScene, self).__init__(parent)
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        self.setSceneRect(-1000, -1000, 2000, 2000)
        oItem = CWidget("联系方式")
        self.addWidget(oItem)

    def _InitSignal(self):
        pass


class CWidget(QtWidgets.QWidget):
    def __init__(self, str="", parent=None):
        super(CWidget, self).__init__(parent)
        self._InitUI()

    def _InitUI(self):
        self.resize(500, 400)
        tellLabel = QLabel("电话号码：", self)
        addrLabel = QLabel("居住地址：", self)
        tellLineEdit = QLineEdit(self)
        addrLineEdit = QLineEdit(self)
        tellLineEdit.setPlaceholderText("手机/固话")
        addrLineEdit.setPlaceholderText("具体到门牌号")
        vBox = QVBoxLayout(self)
        layout1 = QHBoxLayout()
        layout1.addWidget(tellLabel)
        layout1.addWidget(tellLineEdit)
        layout2 = QHBoxLayout()
        layout2.addWidget(addrLabel)
        layout2.addWidget(addrLineEdit)

        vBox.setSpacing(10)
        vBox.setContentsMargins(6, 6, 6, 6)
        vBox.addLayout(layout1)
        vBox.addLayout(layout2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CView()
    obj.show()
    sys.exit(app.exec_())
