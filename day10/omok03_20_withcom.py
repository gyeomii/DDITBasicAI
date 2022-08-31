import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QMessageBox

import numpy as np



form_class = uic.loadUiType("omok03.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.histI = [0,0,0,0,0]
        self.histJ = [0,1,2,3,4]
        self.histIdx = 0
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
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
                
        self.myrender()
        self.pbReset.clicked.connect(self.myreset)
        
        self.show()
        
    def myreset(self):
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0
                
        self.myrender()
        self.flagWb = True
        self.flagIng = True
        self.histIdx = 0
        
        
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                               
                
    def myclick(self):
        if not self.flagIng:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i,j,stone)
        le = self.checkLE(i,j,stone)
        ur = self.checkUR(i,j,stone)
        ul = self.checkUL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flagIng = False
            if self.flagWb:
                QMessageBox.question(self, '오목', "흰돌승리", QMessageBox.Yes, QMessageBox.NoButton)
            else:
                QMessageBox.question(self, '오목', "흑돌승리", QMessageBox.Yes, QMessageBox.NoButton)

            
        
        
        self.flagWb = not self.flagWb
        #-----------------------------------------------------------------------------------------------com
        
        if not self.flagIng:
            return
        

        i = self.histI[self.histIdx]
        j = self.histJ[self.histIdx]
        self.histIdx += 1
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i,j,stone)
        le = self.checkLE(i,j,stone)
        ur = self.checkUR(i,j,stone)
        ul = self.checkUL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flagIng = False
            if self.flagWb:
                QMessageBox.question(self, '오목', "흰돌승리", QMessageBox.Yes, QMessageBox.NoButton)
            else:
                QMessageBox.question(self, '오목', "흑돌승리", QMessageBox.Yes, QMessageBox.NoButton)

            
        
        
        self.flagWb = not self.flagWb
        
        
        
    def checkDL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkDR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
        
    def checkUL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
        
    def checkUR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
        
    def checkLE(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
        
    def checkRI(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
        
    def checkUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def checkDW(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] ==stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    