import sys
import ast
from PyQt4 import QtGui
#from ui.Frame import Window
from traitement.Traitement import CountFunc
#from ui.Frame import CountFunc
from ui import Frame

class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.fc = Frame.CountFunc().GoToPath()
        self.frame = Frame.Window()

if __name__ == '__main__':
    app = App(sys.argv)
    counter = CountFunc()
    sys.exit(app.exec_())