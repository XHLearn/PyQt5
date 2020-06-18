# -*- coding:utf-8 -*-
'''
@Description: 线程运行中，是否可以外部暂停/继续运行线程，测试结果证明可行
    但如果想要重新运行线程程序，需要先停止原来线程(循环检测是否停止)，然后再进行
@Author: lamborghini1993
@Date: 2019-02-22 11:18:03
@UpdateDate: 2019-02-22 16:03:55
'''

import sys
import threading
import time

from PyQt5 import QtWidgets


class CMyLove(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CMyLove, self).__init__(parent)
        self.m_Thread = CMyThread()
        self._InitUI()

    def _InitUI(self):
        vBox = QtWidgets.QVBoxLayout(self)
        btn1 = QtWidgets.QPushButton("播放/暂停", self)
        btn2 = QtWidgets.QPushButton("重新开始", self)
        vBox.addWidget(btn1)
        vBox.addWidget(btn2)
        btn1.clicked.connect(self.S_StartAndPause)
        btn2.clicked.connect(self.S_Restart)

    def S_StartAndPause(self):
        self.m_Thread.StartAndPause()

    def S_Restart(self):
        # print(dir(self.m_Thread))
        self.m_Thread.Stop()
        while self.m_Thread.isAlive():
            print("%s is alive:" % self.m_Thread.name)
            time.sleep(0.5)
        self.m_Thread = CMyThread()


class CMyThread(threading.Thread):
    def __init__(self):
        super(CMyThread, self).__init__()
        self.m_ID = 0
        self.m_bRun = True
        self.m_bPause = False
        self.setDaemon(True)
        self.start()

    def StartAndPause(self):
        self.m_bPause = not self.m_bPause

    def Stop(self):
        self.m_bRun = False

    def run(self):
        print("---%s start---" % self.name)
        while self.m_bRun:
            time.sleep(1)
            if not self.m_bPause:
                print(self.m_ID)
                self.m_ID += 1
        print("---%s end---\n" % self.name)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    obj = CMyLove()
    obj.show()
    sys.exit(app.exec_())
