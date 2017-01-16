import sys
#import ast
from PyQt5.QtWidgets import QApplication
from ui.Frame import Example
#hhhhhhhh
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())