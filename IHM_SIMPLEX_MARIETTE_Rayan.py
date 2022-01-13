# =============================================================================
# Nom du fichier : IHM_SIMPLEX_MARIETTE_Rayan.py
# Auteur : MARIETTE Rayan
# Année : 2021-2022
# Classe : ITS2
# Sujet : Methode Simplexe ' Linear Programming'
# Professeur : Thiago ABREU
# =============================================================================

import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.b1 = QtWidgets.QPushButton("SEND")
        self.x01 = QtWidgets.QLineEdit("0")
        self.x02 = QtWidgets.QLineEdit("0")
        self.x03 = QtWidgets.QLineEdit("0")
        self.x04 = QtWidgets.QLineEdit("0")
        self.x11 = QtWidgets.QLineEdit("0")
        self.x12 = QtWidgets.QLineEdit("0")
        self.x13 = QtWidgets.QLineEdit("0")
        self.x14 = QtWidgets.QLineEdit("0")
        self.x15 = QtWidgets.QLineEdit("=")
        self.x16 = QtWidgets.QLineEdit("0")
        self.x21 = QtWidgets.QLineEdit("0")
        self.x22 = QtWidgets.QLineEdit("0")
        self.x23 = QtWidgets.QLineEdit("0")
        self.x23 = QtWidgets.QLineEdit("0")
        self.x24 = QtWidgets.QLineEdit("0")
        self.x25 = QtWidgets.QLineEdit("=")
        self.x26 = QtWidgets.QLineEdit("0")
        self.x31 = QtWidgets.QLineEdit("0")
        self.x32 = QtWidgets.QLineEdit("0")
        self.x33 = QtWidgets.QLineEdit("0")
        self.x34 = QtWidgets.QLineEdit("0")
        self.x35 = QtWidgets.QLineEdit(">=")
        self.x36 = QtWidgets.QLineEdit("0")
        self.x41 = QtWidgets.QLineEdit("0")
        self.x42 = QtWidgets.QLineEdit("0")
        self.x43 = QtWidgets.QLineEdit("0")
        self.x44 = QtWidgets.QLineEdit("0")
        self.x45 = QtWidgets.QLineEdit(">=")
        self.x46 = QtWidgets.QLineEdit("0")
        self.s = QtWidgets.QLineEdit("max")
                
        self.l1= QtWidgets.QLabel("x1")
        self.l2= QtWidgets.QLabel("x2")
        self.l3= QtWidgets.QLabel("x3")
        self.l4= QtWidgets.QLabel("x4")
        self.l5= QtWidgets.QLabel("Signe")
        self.l6= QtWidgets.QLabel("S")
        self.l7= QtWidgets.QLabel("Z")
        self.l8= QtWidgets.QLabel(" ")
        self.l9= QtWidgets.QLabel(" ")
        self.l10= QtWidgets.QLabel(" ")
        self.l11= QtWidgets.QLabel(" ") 
        self.l12= QtWidgets.QLabel(" ")
        
        h_box0=QtWidgets.QHBoxLayout()    
        h_box0.addWidget(self.x01)
        h_box0.addWidget(self.x02)
        h_box0.addWidget(self.x03)
        h_box0.addWidget(self.x04)
        
        
        h_box=QtWidgets.QHBoxLayout()    
        h_box.addWidget(self.x11)
        h_box.addWidget(self.x12)
        h_box.addWidget(self.x13)
        h_box.addWidget(self.x14)
        h_box.addWidget(self.x15)#
        h_box.addWidget(self.x16)
        
        h_box1=QtWidgets.QHBoxLayout()    
        h_box1.addWidget(self.x21)
        h_box1.addWidget(self.x22)
        h_box1.addWidget(self.x23)
        h_box1.addWidget(self.x24)
        h_box1.addWidget(self.x25)#
        h_box1.addWidget(self.x26)
           
        
        h_box2=QtWidgets.QHBoxLayout()  
        h_box2.addWidget(self.x31)
        h_box2.addWidget(self.x32)
        h_box2.addWidget(self.x33)
        h_box2.addWidget(self.x34)
        h_box2.addWidget(self.x35)#
        h_box2.addWidget(self.x36)
        
        h_txt=QtWidgets.QHBoxLayout() 
        h_txt.addWidget(self.l1)
        h_txt.addWidget(self.l2)
        h_txt.addWidget(self.l3)
        h_txt.addWidget(self.l4)
        h_txt.addWidget(self.l5)
        h_txt.addWidget(self.l6)
        
        h_box4=QtWidgets.QHBoxLayout() 
        h_box4.addWidget(self.x41)
        h_box4.addWidget(self.x42)
        h_box4.addWidget(self.x43)
        h_box4.addWidget(self.x44)
        h_box4.addWidget(self.x45)#
        h_box4.addWidget(self.x46)
        
        h_box5=QtWidgets.QHBoxLayout() 
        h_box5.addWidget(self.b1,8)
        h_box5.addWidget(self.s,2)
        
        
        # h_box6=QtWidgets.QVBoxLayout() 
        # h_box6.addWidget(self.l7)
        # h_box6.addWidget(self.l8)
        # h_box6.addWidget(self.l9)
        # h_box6.addWidget(self.l10)
        # h_box6.addWidget(self.l11)
        # h_box6.addWidget(self.l12)
        

        
        v_box=QtWidgets.QVBoxLayout()
        # v_box.addLayout(h_box6)
        v_box.addLayout(h_txt)
        v_box.addLayout(h_box0)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)        
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)

        self.setLayout(v_box)
        self.b1.clicked.connect(lambda:self.button_click())
        self.setWindowTitle("Simplex")
        self.show()
        
    def button_click(self):

        val_x11=self.x11.text()
        val_x12=self.x12.text()
        val_x13=self.x13.text()
        val_x13=self.x13.text()
        val_x14=self.x14.text()
        val_x15=self.x15.text()
        val_x16=self.x16.text()
        val_x21=self.x21.text()
        val_x22=self.x22.text()
        val_x23=self.x23.text()
        val_x24=self.x24.text()
        val_x25=self.x25.text()
        val_x26=self.x26.text()
        val_x31=self.x31.text()
        val_x32=self.x32.text()
        val_x33=self.x33.text()
        val_x34=self.x34.text()
        val_x35=self.x35.text()
        val_x36=self.x36.text()
        val_x41=self.x41.text()
        val_x42=self.x42.text()
        val_x43=self.x43.text()
        val_x44=self.x44.text()
        val_x45=self.x45.text()
        val_x46=self.x46.text()
        val_s=self.s.text()        
        
        A=[val_x11,val_x12,val_x13,val_x14]
        B=[val_x21,val_x22,val_x23,val_x24]
        C=[val_x31,val_x32,val_x33,val_x34]
        D=[val_x41,val_x42,val_x43,val_x44]
        
        return A,B,C,D
app=QtWidgets.QApplication(sys.argv)
a=window=Window()
sys.exit(app.exec_())

