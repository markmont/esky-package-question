#!/usr/bin/env python

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from helloform import Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())

