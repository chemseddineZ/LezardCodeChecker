#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import ast
import lizard
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QFileDialog, QPushButton, QTextEdit, \
    QLineEdit, QLabel, QTableWidget,QTableWidgetItem)
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5 import QtWidgets, QtGui, QtCore



class Example(QtWidgets.QMainWindow, ast.NodeVisitor):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #self.setFixedSize(300, 200)
        self.setGeometry(300, 300, 620, 400)
        self.setWindowTitle('LezardCodeChecker ;)')

        self.func_count = 0

        OpenFile = QAction('&Open File', self)
        OpenFile.setShortcut('Ctrl+O')
        OpenFile.setStatusTip('Open File')
        OpenFile.triggered.connect(self.File_Open)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(OpenFile)
        fileMenu.addAction(exitAction)


        self.home()

    def home(self):
            self.btn = QtWidgets.QPushButton("Start", self)
            self.btn.clicked.connect(self.change_state)
            self.btn.resize(self.btn.minimumSizeHint())
            self.btn.move(10, 230)
            self.CodePane = QtWidgets.QTextEdit(self)
            #self.setCentralWidget(self.CodePane)
            self.CodePane.setFixedSize(600, 200)
            self.CodePane.move(10, 30)

            self.comments = QtWidgets.QLabel("Comments Count", self)
            self.lines = QtWidgets.QLabel("Lines Count", self)
            self.functions = QtWidgets.QLabel("Functions Count", self)


            '''self.nameFn = QtWidgets.QLabel("", self)
            self.paramsFn = QtWidgets.QLabel("", self)
            self.compFn = QtWidgets.QLabel("", self)
            self.nlocFn = QtWidgets.QLabel("", self)
            self.lengthFn = QtWidgets.QLabel("", self)'''


            self.comments.move(10, 250)
            self.lines.move(10, 290)
            self.functions.move(10, 300)
            #self.fnName.move(10,)

            self.nbcom = QtWidgets.QLineEdit("", self)
            self.validator = QIntValidator()
            self.nbcom.setValidator(self.validator)
            self.nbcom.setMaxLength(5)
            self.nbcom.resize(40, 25)
            #self.nbcom.move(100, 250)
            #self.nbcom.setReadOnly(True)

            self.nblines = QtWidgets.QLineEdit("", self)
            self.nblines.setValidator(self.validator)
            self.nblines.setMaxLength(5)
            self.nblines.resize(40, 25)
            self.nblines.move(80, 290)

            self.nbfunc = QtWidgets.QLineEdit("", self)
            self.nbfunc.setValidator(self.validator)
            self.nbfunc.setMaxLength(5)
            self.nbfunc.resize(40, 25)
            self.nbfunc.move(60, 330)

            self.setCentralWidget(QtWidgets.QFrame())
            self.vlayout = QtWidgets.QVBoxLayout()
            self.hlayout = QtWidgets.QHBoxLayout()
            self.functionsLayout = QtWidgets.QHBoxLayout()

            self.hlayout.addWidget(self.btn)
            self.hlayout.addWidget(self.comments)
            self.hlayout.addWidget(self.nbcom)
            self.hlayout.addWidget(self.lines)
            self.hlayout.addWidget(self.nblines)
            self.hlayout.addWidget(self.functions)
            self.hlayout.addWidget(self.nbfunc)


            '''self.fnName = QtWidgets.QLabel("Function Name", self)
            self.fnParams = QtWidgets.QLabel("Function Parameters", self)
            self.fnComp = QtWidgets.QLabel("Cyclomatic Complexity", self)
            self.fnNloc = QtWidgets.QLabel("NLOC", self)
            self.fnLength = QtWidgets.QLabel("Length", self)'''

            '''self.functionsLayout.addWidget(self.fnName)
            self.functionsLayout.addWidget(self.nameFn)
            self.functionsLayout.addWidget(self.fnParams)
            self.functionsLayout.addWidget(self.paramsFn)
            self.functionsLayout.addWidget(self.fnComp)
            self.functionsLayout.addWidget(self.compFn)
            self.functionsLayout.addWidget(self.fnNloc)
            self.functionsLayout.addWidget(self.nlocFn)
            self.functionsLayout.addWidget(self.fnLength)
            self.functionsLayout.addWidget(self.lengthFn)'''

            self.vlayout.addWidget(self.CodePane)
            self.vlayout.addLayout(self.hlayout)
            self.vlayout.addLayout(self.functionsLayout)

            self.centralWidget().setLayout(self.vlayout)


            self.show()

    def change_state(self):
        '''print("comments Count:", self.commentCount)
        print("commentCount Format: ", type(self.commentCount))
        print("Line Count:", self.numl)
        print("Functions count:", self.func_count)'''
        #self.home()
        self.nbcom.setText(str(self.commentCount))
        self.nblines.setText(str(self.numl))
        self.nbfunc.setText((str(self.func_count)))

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.func_count)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels( ["Function Name", "Prameters", "Cyclomatic Complexity",
                                                     "NLOC", "Length"])

        for j in range(self.func_count):

            self.tableWidget.setItem(j, 0, QTableWidgetItem(self.i.function_list[j].__dict__['long_name']))
            self.tableWidget.setItem(j, 1, QTableWidgetItem(str(self.i.function_list[j].__dict__['parameters'])))
            self.tableWidget.setItem(j, 2, QTableWidgetItem(str(self.i.function_list[j].__dict__['cyclomatic_complexity'])))
            self.tableWidget.setItem(j, 3, QTableWidgetItem(str(self.i.function_list[j].__dict__['nloc'])))
            self.tableWidget.setItem(j, 4, QTableWidgetItem(str(self.i.function_list[j].__dict__['length'])))



        self.vlayout.addWidget(self.tableWidget)


    def File_Open(self):
            self.numl = 0
            self.commentCount = 0;
            self.name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')[0]
            self.home()

            with open(self.name, 'r') as file:
                print("file name :", self.name)
                for eachLine in file:  # loops the lines in the file object ans sets the pointer to the end of the file
                    if eachLine.strip():  # check if the line is a blank line
                        self.numl += 1
                    if eachLine.find('#') != -1:  # looks to find the comment tag
                        self.commentCount += 1
                print("number of comments %i" % self.commentCount)
                print("num lines %i: " % self.numl)

                # print(self.nbcom.text())
                # print(self.nblines.text())
                # print("nbcom : ", self.commentCount)
                # print("nblines : ", self.numl)
                file.seek(0, 0)  # resets the pointer to the beginning of the file so we can read it again
                self.text = file.read()
                self.CodePane.setText(self.text)
                self.GoToPath()

    def visit_FunctionDef(self, node):
            self.func_count += 1

    def GoToPath(self):
            p = ast.parse(self.text)
            self.visit(p)
            print("number of functions:", self.func_count)
            # print("my name is", self.GoToPath.__name__)
            # print(self.path)


            self.i = lizard.analyze_file(self.name)
            if (self.func_count > 0):
                for j in range(self.func_count):
                    # print(i.function_list[j].__dict__)
                    print("Function Name: ", self.i.function_list[j].__dict__['long_name'],
                          "Paramètres:", self.i.function_list[j].__dict__['parameters'],
                          "Cyclomatic Comlexity: ", self.i.function_list[j].__dict__['cyclomatic_complexity'],
                          "Number of line of code: ", self.i.function_list[j].__dict__['nloc'],
                          "Length: ", self.i.function_list[j].__dict__['length'])
            else:
                print("Ce fichier ne contitent pas de fonctions")

