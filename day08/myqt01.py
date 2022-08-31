import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from day08.mymnist_hit_load_class import HerKY

form_class = uic.loadUiType("myqt01.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.hky = HerKY()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):   
        
        mine = self.le_mine.text()
        com = ""
        
        ans = -1
        if mine == "1": ans = self.hky.guess([[1,0,0,0,0    ,0,0,0,0]])
        if mine == "2": ans = self.hky.guess([[0,1,0,0,0    ,0,0,0,0]])
        if mine == "3": ans = self.hky.guess([[0,0,1,0,0    ,0,0,0,0]])
        
        if mine == "4": ans = self.hky.guess([[0,0,0,1,0    ,0,0,0,0]])
        if mine == "5": ans = self.hky.guess([[0,0,0,0,1    ,0,0,0,0]])
        if mine == "6": ans = self.hky.guess([[0,0,0,0,0    ,1,0,0,0]])

        if mine == "7": ans = self.hky.guess([[0,0,0,0,0    ,0,1,0,0]])
        if mine == "8": ans = self.hky.guess([[0,0,0,0,0    ,0,0,1,0]])
        if mine == "9": ans = self.hky.guess([[0,0,0,0,0    ,0,0,0,1]])
            
        if ans == 0 :   com = "1"
        if ans == 1 :   com = "2"
        if ans == 2 :   com = "3"
        if ans == 3 :   com = "4"
        if ans == 4 :   com = "5"
        if ans == 5 :   com = "6"
        if ans == 6 :   com = "7"
        if ans == 7 :   com = "8"
        if ans == 8 :   com = "9"
        
        self.le_com.setText(com)

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()