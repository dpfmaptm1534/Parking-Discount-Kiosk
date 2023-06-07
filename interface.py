import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox,QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from car import *
from car2t import *
from car5t import *
from time import sleep
from PyQt5 import uic
import chromedriver_autoinstaller
#test=cargo
#pip install chromedriver-autoinstaller
import os
from shutil import move

# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
print(chrome_ver)
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)
    move(driver_path,'./chromedriver.exe')
class comwin1(QDialog):
    def __init__(self, parent , carnum):
        self.carnum=carnum
        super(comwin1, self).__init__(parent)
        uic.loadUi("C:\carinterface\listok.ui", self)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog",self.carnum + " 전액감면완료"))
        self.show()

class comwin2(QDialog):
    def __init__(self, parent , carnum):
        self.carnum=carnum
        super(comwin2, self).__init__(parent)
        uic.loadUi("C:\carinterface\listok.ui", self)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog",self.carnum + " 2시간감면완료"))
        self.show() 
 
class comwin3(QDialog):
    def __init__(self, parent , carnum):
        self.carnum=carnum
        super(comwin3, self).__init__(parent)
        uic.loadUi("C:\carinterface\listok.ui", self)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog",self.carnum + " 50%할인완료"))
        self.show() 
               
class liok(QDialog):
    def __init__(self, parent):
        super(liok, self).__init__(parent)
        uic.loadUi("C:\carinterface\listok.ui", self)
        self.show()      

class LoadingScreen(QWidget):
        def __init__(self):
            super().__init__()
            self.setFixedSize(200,200)
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
            self.label_animation = QLabel(self) 
            self.movie=QMovie('Loading_2.gif')
            self.label_animation.setMovie(self.movie)
            timer = QTimer(self)
            self.startAnimation()
            timer.singleShot(3000, self.stopAnimation)
            self.show()

        def startAnimation(self):
            self.movie.start()

        def stopAnimation(self):
            self.movie.stop()
            self.close()

class MainWindow(QDialog):
    
    #onelist = []
    
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("aaa.ui",self)
        self.onelist = []
        self.carlists = []
        self.stroncarnum=''
        self.cou=0
        #self.pushButton_search.clicked.connect(self.gotoScreen2)
        self.pushButton_1.clicked.connect(self.method_1)
        self.pushButton_2.clicked.connect(self.method_2)
        self.pushButton_3.clicked.connect(self.method_3)
        self.pushButton_4.clicked.connect(self.method_4)
        self.pushButton_5.clicked.connect(self.method_5)
        self.pushButton_6.clicked.connect(self.method_6)
        self.pushButton_7.clicked.connect(self.method_7)
        self.pushButton_8.clicked.connect(self.method_8)
        self.pushButton_9.clicked.connect(self.method_9)
        self.pushButton_0.clicked.connect(self.method_0)
        self.pushButton_arrow.clicked.connect(self.method_arrow)
        self.pushButton_search.clicked.connect(self.method_search)
        self.box_1.setText("")
        self.box_2.setText("")
        self.box_3.setText("")
        self.box_4.setText("")

    def innum(self,a):
        if(len(self.onelist)<=3):
            self.onelist.append(a)

    def lnumtostr(self):
        #print('class1_startlnumtostr')
        bbb=list(map(str,self.onelist))
        s="".join(bbb)
        #print('print bbb ' + str(s))
        return str(s)

    def passtocar(self,carnum):
        

        test=cargo(carnum)
        #print('lnumtostr_startcarpy')
        #test.start()
        #print('lnumtostr_endcarpy')
        self.cou=test.countnum
        #print('lnumtostr_print self.cou= ' + str(self.cou))
        self.carlists=test.numlist
        #print('lnumtostr_.print self.carlists = ' + str(self.carlists))
        #print('lnumtostr_.testend')
        
    def outnum(self):
        try:
            self.onelist.pop()
        except:
            print("더이상지울게없어요")

    def method_arrow(self):
        self.outnum()
        self.listdel()

    def method_1(self):
        self.innum(1)
        self.listinput()
        print(self.onelist)

    def method_2(self):
        self.innum(2)
        self.listinput()
        print(self.onelist)

    def method_3(self):
        self.innum(3)
        self.listinput()
        print(self.onelist)

    def method_4(self):
        self.innum(4)
        self.listinput()
        print(self.onelist)

    def method_5(self):
        self.innum(5)
        self.listinput()
        print(self.onelist)

    def method_6(self):
        self.innum(6)
        self.listinput()
        print(self.onelist)

    def method_7(self):
        self.innum(7)
        self.listinput()
        print(self.onelist)

    def method_8(self):
        self.innum(8)
        self.listinput()
        print(self.onelist)

    def method_9(self):
        self.innum(9)
        self.listinput()
        print(self.onelist)

    def method_0(self):
        self.innum(0)
        self.listinput()
        print(self.onelist)

    def listinput(self):
        if len(self.onelist)==1:
            self.box_1.setText(str(self.onelist[0]))
        elif len(self.onelist)==2:
            self.box_1.setText(str(self.onelist[0]))
            self.box_2.setText(str(self.onelist[1]))
        elif len(self.onelist)==3:
            self.box_1.setText(str(self.onelist[0]))
            self.box_2.setText(str(self.onelist[1]))
            self.box_3.setText(str(self.onelist[2]))
        elif len(self.onelist)==4:
            self.box_1.setText(str(self.onelist[0]))
            self.box_2.setText(str(self.onelist[1]))
            self.box_3.setText(str(self.onelist[2]))
            self.box_4.setText(str(self.onelist[3]))
        
    def listdel(self):
        if len(self.onelist)==0:
            self.box_1.setText("")
        elif len(self.onelist)==1:
            self.box_2.setText("")
        elif len(self.onelist)==2:
            self.box_3.setText("")
        elif len(self.onelist)==3:
            self.box_4.setText("")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.box_1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.box_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.box_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.box_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
   
    def method_search(self):

        self.loading_screen=LoadingScreen()
        self.show()

        #print('metodh_search_method call lnumtostr')
        passnum=self.lnumtostr()
        #print('class1_method_search passnum = ' + str(passnum))
        self.passtocar(passnum)
        self.gotoScreen2()

    def gotoScreen2(self):
        
        onelist=self.lnumtostr()
        screen2=Screen2(onelist,self.carlists)
        #print('goscr2 carlists' + str(self.carlists))
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QDialog):
    
    def __init__(self,onelist,carlists):
            super(Screen2,self).__init__()
            loadUi("button.ui",self)
            self.listWidget.setObjectName("listWidget")
            self.onelist=onelist
            #print('scr2_print self.onelists = ' + str(self.onelist))
            self.carlists=carlists
            #print('scr2_print self.carlists = ' + str(self.carlists))
        #use for_blank

            countnum=len(self.carlists)
            nnn=countnum
            #print('scr2_nnn='+str(nnn))
            #print(type(nnn))
            self.pushButton.clicked.connect(self.gotoex)   #전액
            self.pushButton_3.clicked.connect(self.goto2)  #2시간
            self.pushButton_4.clicked.connect(self.goto50) #50%할인
            self.pushButton_2.clicked.connect(self.gotoScreen1)
            
            
            if nnn>0:
                for i in range(0,nnn):
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setFamily("a아시아고딕L")
                    font.setPointSize(50)
                    item.setFont(font)
                    self.listWidget.addItem(item)
                    #print('nnn>0')
                    
                    
            else:
                item = QtWidgets.QListWidgetItem()
                font = QtGui.QFont()
                font.setFamily("a아시아고딕L")
                font.setPointSize(20)
                item.setFont(font)
                self.listWidget.addItem(item)
                #print('else')    
        #use for_text
            if nnn>0:
                for i in range(0,nnn):
                    _translate = QtCore.QCoreApplication.translate
                    item = self.listWidget.item(i)
                    #print('usefortext '+str(self.carlists[i]))
                    item.setText(_translate("Dialog", str(self.carlists[i])))
            else:
                    _translate = QtCore.QCoreApplication.translate
                    item = self.listWidget.item(0)
                    item.setText(_translate("Dialog", "등록된 차량이 없습니다"))

            item.setSelected
    # def cho(self):
    #     chom = QMessageBox(parent=self)
    #     chom.setTextFormat(2)
    #     chom.setText("<font size=\"15\"> 목록에서 차량을 </font><font size=\"15\" color=\"#8A0808\">선택</font> <font size=\"15\">하십시요 </font> <br><br>")
    #     chom.show()
    #     chom.exec_()
    #     QDialog.show(self)                   
    def liwin(self):
        liok (self)
    def cw1(self, carnum1):
        comwin1(self, carnum1)
    def cw2(self, carnum1):
        comwin2(self, carnum1)
    def cw3(self, carnum1):
        comwin3(self, carnum1)            
    def gotoex(self):
                    try:
                        self.loading_screen=LoadingScreen()
                        self.show()
                        aka=str(self.listWidget.currentItem().text())
                        exex=cargo(aka)
                        #exex()
                        exex.exempt()
                        print('gotoex completed ' + aka)
                        
                        self.cw1(aka)
                        #abc=QMessageBox(parent=self)
                        #abc.question(self, 'success',"<font size=\"15\">" + aka + "차량<br>감면완료되었습니다", abc.Yes)
                        
                        self.gotoScreen1()   
                    except:                        
                        self.liwin()
                        #self.cho()
                        
                        #QMessageBox.critical(self, 'error', "목록에서 차량을 선택하십시요", QMessageBox.Yes)
                        #self.show()
    def goto2(self):
                    try:
                        self.loading_screen=LoadingScreen()
                        self.show()
                        aka=str(self.listWidget.currentItem().text())
                        exex=cargo2(aka)
                        #exex()
                        exex.exempt()
                        print('gotoex completed ' + aka)
                        #QMessageBox.question(self, 'success', aka +"차량 2시간 감면 완료", QMessageBox.Yes)
                        
                        self.cw2(aka)
                        # abc=QMessageBox(parent=self)
                        # abc.question(self, 'success',"<font size=\"15\">" + aka + "차량<br>2시간 감면 완료", abc.Yes)
                        
                        self.gotoScreen1()   
                    except:
                        self.liwin()
                        #self.cho()
                        #QMessageBox.critical(self, 'error', "목록에서 차량을 선택하십시요", QMessageBox.Yes)
                        #self.show()
    def goto50(self):
                    try:
                        self.loading_screen=LoadingScreen()
                        self.show()
                        aka=str(self.listWidget.currentItem().text())
                        exex=cargo50(aka)
                        #exex()
                        exex.exempt()
                        print('gotoex completed ' + aka)
                        #QMessageBox.question(self, 'success', aka +"차량 주차 50%할인 되었습니다", QMessageBox.Yes)
                        
                        self.cw3(aka)
                        # abc=QMessageBox(parent=self)
                        # abc.question(self, 'success',"<font size=\"15\">" + aka + "차량<br>50%할인 감면 완료", abc.Yes)    
                                            
                        self.gotoScreen1()   
                    except:
                        self.liwin()
                        #self.cho()
                        #QMessageBox.critical(self, 'error', "목록에서 차량을 선택하십시요", QMessageBox.Yes)
                        #self.show()                
    def gotoScreen1(self):
        self.loading_screen=LoadingScreen()
        self.show()
        mainwindow=MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)  # 1을 더해주는게 핵심
        try:
            del mainwindow.onelist[:]
        except:
            print("nothinglist")        

app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
#screen2=Screen2()
widget.addWidget(mainwindow)
#widget.addWidget(screen2)
widget.setFixedHeight(1040)
widget.setFixedHeight(701)
widget.move(3200,0)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")