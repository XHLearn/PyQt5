# -*- coding:utf-8 -*-
'''
@Description: 样例
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-03-06 21:05:43
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class CMyLove(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self._InitUI()
        self._InitSignal()

    def _InitUI(self):
        pass

    def _InitSignal(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
