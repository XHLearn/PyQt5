# -*- coding:utf-8 -*-
'''
@Description: 多选下拉菜单的实现
@Author: lamborghini1993
@Date: 2019-03-12 13:45:56
@UpdateDate: 2019-03-12 13:58:53
'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class CMyLove(QtWidgets.QWidget):
    m_IDAttr = "m_ID"

    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self.m_Info = {x: "Test_"+str(x) for x in range(100)}
        self.m_Select = []
        self._InitUI()

    def _InitUI(self):
        hBox = QtWidgets.QHBoxLayout(self)
        self.m_LineEdit = QtWidgets.QLineEdit(self)
        self.m_MenuBtn = QtWidgets.QPushButton(self)
        hBox.addWidget(self.m_LineEdit)
        hBox.addWidget(self.m_MenuBtn)

        self.m_Menu = QtWidgets.QMenu(self)
        for ID, sInfo in self.m_Info.items():
            action = QtWidgets.QAction(sInfo, self)
            action.setCheckable(True)
            self.m_Menu.addAction(action)
            setattr(action, self.m_IDAttr, ID)
            action.triggered.connect(self.S_StateChanged)
        self.m_MenuBtn.setMenu(self.m_Menu)

    def S_StateChanged(self, bChecked):
        send = self.sender()
        ID = getattr(send, self.m_IDAttr)
        if bChecked:
            self.m_Select.append(ID)
        else:
            self.m_Select.remove(ID)
        self.m_Select = sorted(self.m_Select)
        lstTemp = [str(x) for x in self.m_Select]
        self.m_LineEdit.setText("&".join(lstTemp))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
