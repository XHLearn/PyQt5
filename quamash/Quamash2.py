# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-14 19:44:23
@UpdateDate: 2020-05-15 20:33:39
'''
import asyncio
import shutil
import sys

import quamash
from PyQt5 import QtWidgets


async def do_copy(target):
    for i in range(10):
        loop = asyncio.get_event_loop()
        await asyncio.sleep(0.1, loop=loop)
        print(f'copy {target} at loop {i}')
        shutil.copy('C:/TMP/a.mp4', f'C:/TMP/{target}.mp4')
    return f'copy {target} done'

async def async_copy():
    loop = asyncio.get_event_loop()
    print(loop, id(loop))
    await asyncio.sleep(0.1, loop=loop)
    for i in range(10):
        await do_copy(i)

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        btn_copy = QtWidgets.QPushButton('Copy', self)
        btn_copy.resize(btn_copy.sizeHint())
        btn_copy.move(50, 50)
        btn_copy.clicked.connect(self.btn_copy_clicked)
        btn_alert = QtWidgets.QPushButton('Alert', self)
        btn_alert.resize(btn_alert.sizeHint())
        btn_alert.move(150, 50)
        btn_alert.clicked.connect(self.btn_alert_clicked)
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def btn_copy_clicked(self, b_checked):
        asyncio.ensure_future(async_copy(), loop=loop)
    def btn_alert_clicked(self, b_checked):
        QtWidgets.QMessageBox().information(self, '提示', 'UI响应了')
        
app = QtWidgets.QApplication(sys.argv)
loop = quamash.QEventLoop(app)
print(loop, id(loop))
asyncio.set_event_loop(loop)  # NEW must set the event loop
asyncio._set_running_loop(loop)
with loop:
    w = Example()
    w.show()
    loop.run_forever()
print('Coroutine has ended')
