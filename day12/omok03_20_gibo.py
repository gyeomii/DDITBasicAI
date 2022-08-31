import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QMessageBox

import numpy as np
from day12.myfile_gibo_class import RaoGibo



form_class = uic.loadUiType("omok03.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        rg = RaoGibo()
        self.arr_i,self.arr_j=rg.getGibo("0_0_1_2.psq")

        self.idx_g = 0
        self.flagWb = True
        self.flagIng = True
        self.arr2D = np.zeros((20,20))
        self.pb2D = []
        self.setupUi(self)
        
        for i in range(20):
            line = []
            for j in range(20):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setToolTip("{},{}".format(i,j))
                line.append(btn)
            self.pb2D.append(line)
                
        self.myrender()
        self.pbReset.clicked.connect(self.mygibo)
        
        self.show()
        
    def mygibo(self):
        print(len(self.arr_i),self.idx_g)
        if len(self.arr_i) <= self.idx_g:
            return
        
        i = self.arr_i[self.idx_g]
        j = self.arr_j[self.idx_g]
        if self.flagWb :   
            self.arr2D[i][j] = 1
        else :
            self.arr2D[i][j] = 2
            
            

        self.myrender()
        self.idx_g += 1
        
        if len(self.arr_i) == self.idx_g:
            if self.flagWb:
                QMessageBox.question(self, '오목', "흰돌승리", QMessageBox.Yes, QMessageBox.NoButton)
            else:
                QMessageBox.question(self, '오목', "흑돌승리", QMessageBox.Yes, QMessageBox.NoButton)
        
        self.flagWb = not self.flagWb
        
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                               

        
        

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    