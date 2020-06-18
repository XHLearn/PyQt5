# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2019-06-24 15:41:39
@UpdateDate: 2019-06-24 16:15:49
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class CMyLove(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self.setAcceptDrops(True)
        self._InitUI()

    def _InitUI(self):
        self.resize(800, 500)
        hBox = QtWidgets.QHBoxLayout(self)
        item = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        widget = CSubLove(self)
        hBox.addItem(item)
        hBox.addWidget(widget)

    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        print("parent Enter")
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)

    def dropEvent(self, event):
        super().dropEvent(event)
        print("parent Drop")


class CSubLove(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(QtCore.QSize(400, 400))
        self.setStyleSheet("background-color:red;")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        super().dragEnterEvent(event)
        print("child Enter")
        event.acceptProposedAction()

    def dragMoveEvent(self, event):
        super().dragMoveEvent(event)

    def dropEvent(self, event):
        super().dropEvent(event)
        print("child drop")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
