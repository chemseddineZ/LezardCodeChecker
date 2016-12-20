import sys
from PyQt4 import QtGui
from ui.Frame import Window
from ui.Frame import CountFunc


class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.frame = Window()
        self.cf = CountFunc()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())