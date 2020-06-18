# -*- coding:utf-8 -*-
'''
@Description: 颜色渐变
@Author: lamborghini1993
@Date: 2019-04-11 20:00:38
@UpdateDate: 2019-04-11 20:53:11

方法，设置一个定时器，添加完毕之后定时之后获取（不在同一帧）
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets


QSS = """
QWidget{
    background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 104, 183, 200), stop:1 rgba(0, 160, 233, 50));
}
"""


class CMyLove(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self.setStyleSheet(QSS)
        self.setGeometry(300, 200, 50, 300)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
