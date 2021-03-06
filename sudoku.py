#! python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sudoku.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem
from sudoku_generator import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        font = QtGui.QFont()
        font.setPointSize(24)
        
        self.board = []
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 451, 451))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.setFont(font)
        
        
        
        self.tableWidget.setItem(0,0, QTableWidgetItem(2))
        
        self.new_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_game_button.setGeometry(QtCore.QRect(490, 360, 200, 75))
        
        self.new_game_button.setFont(font)
        self.new_game_button.setObjectName("new_game_button")
        
        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.solve_button.setGeometry(QtCore.QRect(490, 240, 200, 75))
        self.solve_button.setFont(font)
        self.solve_button.setObjectName("solve_button")
        
        self.clue_label = QtWidgets.QLabel(self.centralwidget)
        self.clue_label.setGeometry(QtCore.QRect(490, 40, 111, 51))
        font_12 = QtGui.QFont()
        font_12.setPointSize(12)
        self.clue_label.setFont(font_12)
        self.clue_label.setObjectName("clue_label")
        
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(490, 110, 181, 41))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(20,80)
        
        self.clue_number_label = QtWidgets.QLabel(self.centralwidget)
        self.clue_number_label.setGeometry(QtCore.QRect(600, 40, 61, 51))
        self.clue_number_label.setFont(font_12)
        self.clue_number_label.setObjectName("clue_number_label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged.connect(self.clue_number_label.setNum)
        self.new_game_button.clicked.connect(lambda: self.new_game(MainWindow, self.horizontalSlider.value()))
        self.solve_button.clicked.connect(lambda: self.solve(MainWindow))
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku Game"))
        self.new_game_button.setText(_translate("MainWindow", "New Game"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.clue_label.setText(_translate("MainWindow", "# of Clues: "))
        self.clue_number_label.setText(_translate("MainWindow", "20"))


    def new_game(self, MainWindow, n):
        self.board = generate_sudoku(n)
        
        
        for row, items in (enumerate(self.board)):
            for col, item in enumerate(items):
                if item == '':
                    self.tableWidget.setItem(row, col, QTableWidgetItem(''))
                    continue
                item = QTableWidgetItem(item)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(row, col, QTableWidgetItem(item))
                
                
                
    def solve(self, MainWindow):
        
        
        VALID_INPUT = {'1','2','3','4','5','6','7','8','9'}
        board = [['' for i in range(9)] for j in range(9)]
        
        for x in range(9):
            for y in range(9):
                
                board[x][y] = self.tableWidget.item(x,y).text()
                if board[x][y] not in VALID_INPUT:
                
                    board = self.board
                    break       
                
        if board != self.board and is_valid_sudoku(board):
            QtWidgets.QMessageBox.about(MainWindow, "Success!", "You've complete the sudoku puzzle!")
            print ('1')
            return 
        
        
        if self.solve_helper(board):
            print ('2')
            return
        else:
            print ("wrong")
            self.solve_helper(self.board)
        
    
    def solve_helper(self, board):
        
        row, col = untested(board)
        
        if row == -1 and col == -1:
            return True
            
        for num in range(1, 10):
            num_str = str(num)
            if is_valid(board, row, col, num_str):
                board[row][col] = num_str
                item = QTableWidgetItem(num_str)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setBackground(QtGui.QBrush(QtGui.QColor("red")))
                self.tableWidget.setItem(row, col, QTableWidgetItem(item))
                self.tableWidget.item(row,col).setText(num_str)
                #self.tableWidget.update()
                
                if self.solve_helper(board):
                    return True
                else:
                    board[row][col] = ''       
                    item = QTableWidgetItem('')
                    self.tableWidget.setItem(row, col, QTableWidgetItem(item))
        return False
            
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    