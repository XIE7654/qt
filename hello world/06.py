# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        # 然后把自己窗口的中心点放置到qr的中心点。
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())