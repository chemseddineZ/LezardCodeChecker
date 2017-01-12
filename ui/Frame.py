import sys
import ast
from PyQt4 import QtGui, QtCore
from radon.visitors import ComplexityVisitor
from radon.complexity import cc_rank, cc_visit
import lizard


class Window(QtGui.QMainWindow, ast.NodeVisitor):

    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(600,500)
        self.setGeometry(50, 50, 600, 300)
        self.setWindowTitle("PyQT!")

        self.func_count = 0


        Exit = QtGui.QAction("&Exit", self)
        Exit.setShortcut("Ctrl+Q")
        Exit.setStatusTip('Quit')
        Exit.triggered.connect(self.close_application)

        OpenFile = QtGui.QAction("&Open File", self)
        OpenFile.setShortcut("Ctrl+O")
        OpenFile.setStatusTip("Open File")
        OpenFile.triggered.connect(self.File_Open)

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(Exit)
        fileMenu.addAction(OpenFile)


        self.home()



    def home(self):
        '''self.btn = QtGui.QPushButton("Start", self)
        self.btn.clicked.connect(self.start_checking)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.move(10, 230)'''
        self.CodePane = QtGui.QTextEdit(self)
        self.setCentralWidget(self.CodePane)
        self.CodePane.setFixedSize(600, 200)
        self.CodePane.move(10, 30)


        self.comments = QtGui.QLabel("Comments Count : ", self)
        self.lines = QtGui.QLabel("Lines Count : ", self)
        self.nbcom = QtGui.QLabel(self)
        self.nblines = QtGui.QLabel(self)
        self.comments.move(10, 250)
        self.lines.move(10, 270)
        self.nbcom.move(30, 250)
        self.nblines.move(30, 270)


        self.show()


    def close_application(self):
        sys.exit()

    def File_Open(self):
        numl = 0
        commentCount = 0;
        self.name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.home()


        with open(self.name, 'r') as file:
            print("file name :", self.name)
            for eachLine in file:  # loops the lines in the file object ans sets the pointer to the end of the file
                if eachLine.strip():  # check if the line is a blank line
                    numl += 1
                if eachLine.find('#') != -1:  # looks to find the comment tag
                    commentCount += 1
            print("number of comments %i" % commentCount)
            print("num lines %i: "% numl)
            file.seek(0, 0) #resets the pointer to the beginning of the file so we can read it again
            self.text = file.read()
            self.CodePane.setText(self.text)
            self.GoToPath()




    def visit_FunctionDef(self, node):
        self.func_count += 1


    def GoToPath(self):
        p = ast.parse(self.text)
        self.visit(p)
        print("number of functions:", self.func_count)
        #print("my name is", self.GoToPath.__name__)
        #print(self.path)


        i = lizard.analyze_file(self.name)
        if (self.func_count > 0):
            for j in range(self.func_count):
                #print(i.function_list[j].__dict__)
                print("Function Name: ", i.function_list[j].__dict__['long_name'],
                    "Paramètres:", i.function_list[j].__dict__['parameters'],
                     "Cyclomatic Comlexity: ", i.function_list[j].__dict__['cyclomatic_complexity'],
                     "Number of line of code: ", i.function_list[j].__dict__['nloc'],
                     "Length: ", i.function_list[j].__dict__['length'])
        else: print("Ce fichier ne contitent pas de fonctions")




