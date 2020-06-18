# -*- coding:utf-8 -*-
'''
@Description: 多选下拉框
@Author: lamborghini1993
@Date: 2019-03-06 21:00:38
@UpdateDate: 2019-03-14 13:46:17
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class CMyLove(QtWidgets.QWidget):
    m_IDAttr = "m_ID"

    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self.combobox = None
        self.lineedit = None
        self.select = []
        self.iteminfo = {}
        self.resize(500, 50)
        self._InitUI2()
        self._ShowText()

    def _ShowText(self):
        self.select = sorted(self.select)
        tmplst = [str(x) for x in self.select]
        self.lineedit.setText("&".join(tmplst))

    def _InitUI(self):
        self.combobox = combox = QtWidgets.QComboBox(self)
        listWidget = QtWidgets.QListWidget(self)
        self.lineedit = QtWidgets.QLineEdit(self)
        for x in range(100):
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            listWidget.addItem(item)
            sName = "Test_"+str(x)
            checkbox = QtWidgets.QCheckBox(sName, self)
            setattr(checkbox, self.m_IDAttr, x)
            listWidget.setItemWidget(item, checkbox)
            checkbox.toggled.connect(self.S_StateChanged)
        combox.setModel(listWidget.model())
        combox.setView(listWidget)
        combox.setLineEdit(self.lineedit)
        self.lineedit.setReadOnly(True)

        hBox = QtWidgets.QVBoxLayout(self)
        hBox.addWidget(combox)

    def S_StateChanged(self, value):
        checkbox = self.sender()
        ID = getattr(checkbox, self.m_IDAttr)
        if value:
            self.select.append(ID)
        else:
            self.select.remove(ID)
        self._ShowText()

    def _InitUI2(self):
        self.combobox = combox = QtWidgets.QComboBox(self)
        listWidget = QtWidgets.QListWidget(self)
        self.lineedit = QtWidgets.QLineEdit(self)
        index = 0
        for x in range(100):
            sName = "Test_"+str(x)
            item = QtWidgets.QListWidgetItem(listWidget)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setText(sName)
            setattr(item, self.m_IDAttr, x)
            if x in self.select:
                item.setCheckState(QtCore.Qt.Checked)
            listWidget.addItem(item)
            self.iteminfo[index] = item
            index += 1

        combox.setModel(listWidget.model())
        combox.setView(listWidget)
        combox.setLineEdit(self.lineedit)
        self.lineedit.setReadOnly(True)

        hBox = QtWidgets.QVBoxLayout(self)
        hBox.addWidget(combox)

        combox.activated.connect(self.S_Activated)

    def S_Activated(self, index):
        item = self.iteminfo[index]
        ID = getattr(item, self.m_IDAttr)
        value = item.checkState()
        if value == QtCore.Qt.Checked:
            self.select.remove(ID)
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.select.append(ID)
            item.setCheckState(QtCore.Qt.Checked)
        self._ShowText()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
