import sys
import ast
from PyQt4 import QtGui, QtCore
from radon.visitors import ComplexityVisitor


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT!")
        Exit = QtGui.QAction("&Exit", self)
        Exit.setShortcut("Ctrl+Q")
        Exit.setStatusTip('Quit')
        Exit.triggered.connect(self.close_application)

        OpenFile = QtGui.QAction("&Open File", self)
        OpenFile.setShortcut("Ctrl+O")
        OpenFile.setStatusTip("Open File")
        OpenFile.triggered.connect(self.File_Open)

        OpenEditor = QtGui.QAction("&Editor", self)
        OpenEditor.setShortcut("Ctrl+E")
        OpenEditor.setStatusTip("Open Editor")
        OpenEditor.triggered.connect(self.editor)
        #self.statusBar()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(Exit)
        fileMenu.addAction(OpenFile)

        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(OpenEditor)
        self.show()
       # self.home()

    '''def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(100, 100)
        btn.move(0, 100)
        self.show()
'''
    def close_application(self):
        print("bye bye !")
        sys.exit()

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def File_Open(self):
        numl = 0
        commentCount = 0;
        self.name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        #file = open(name, 'r')

        self.editor()
        defCount = 0


        with open(self.name, 'r') as file:

            '''file.seek(0, 0)
            text = file.read()
            v = ComplexityVisitor.from_code(text)
            print(v.functions)'''

            for eachLine in file:
                #loops the lines in the file object ans sets the pointer to the end of the file
                if eachLine.strip(): #check if the line is a blank line
                 numl += 1
                if eachLine.find('#') != -1: #looks to find the comment tag
                    commentCount += 1
            print("number of comments %i" % commentCount)
            print("num lines %i: "% numl)

            file.seek(0, 0) #resets the pointer to the beginning of the file so we can read it again
            text = file.read()
            self.textEdit.setText(text)
            #tree = ast.parse(text)
            #print(sum(isinstance(exp, ast.FunctionDef)for exp in tree.body))

        #function_counter = CountFunc(self.name)


class CountFunc(ast.NodeVisitor):
    def __init__(self):
        self. func_count = 0
        self.path = "../ui/Frame.py"


    def visit_FunctionDef(self, node):
        self.func_count += 1

    def GoToPath(self):
        p = ast.parse(open(self.path).read())
        self.visit(p)
        print("number of functions:", self.func_count)
        #p = ast.parse(open(path).read())


'''def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    f = CountFunc()
    f.GoToPath()
    sys.exit(app.exec_())

run()'''
