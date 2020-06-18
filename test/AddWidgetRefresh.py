# -*- coding:utf-8 -*-
'''
@Description: 添加控件之后获取相对父控件坐标
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-04-10 20:56:16

方法，设置一个定时器，添加完毕之后定时之后获取（不在同一帧）
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QPushButton, QSpacerItem, QVBoxLayout, QSizePolicy


class CMyLove(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self.m_Num = 0
        self.m_Lst = []
        self._InitUI()

    def _InitUI(self):
        self.setGeometry(300, 200, 500, 300)
        self.m_Box = QVBoxLayout(self)
        btn = QPushButton("+", self)
        self.m_Box.addWidget(btn)
        btn.clicked.connect(self.S_Add)
        item = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.m_Box.addItem(item)

    def S_Add(self):
        """同一帧添加的控件获取相对父控件位置为0"""
        self.m_Num += 1
        btn = QPushButton("Test"+str(self.m_Num), self)
        self.m_Box.insertWidget(self.m_Num, btn)
        self.m_Lst.append(btn)
        for btn in self.m_Lst:
            # pos = btn.mapToParent(QPoint(0, 0))
            pos = btn.pos()
            print("%s 相对父控件坐标:" % btn.text(), pos.x(), pos.y())
        print("-"*50)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
