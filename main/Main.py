import sys
import ast
from PyQt4 import QtGui
from ui.Frame import Window
from ui import Frame


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    frame = Window()
    frame.show()
    sys.exit(app.exec_())