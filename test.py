# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/carinterface/aaa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from car import *

test=cargo


class Ui_Dialog(object):

    nlist = []

    def innum(self,a):
        if(len(self.nlist)<=3):
            self.nlist.append(a)


    def outnum(self):
        try:
            self.nlist.pop()
        except:
            print("더이상지울게없어요")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1040, 701)
        Dialog.setMinimumSize(QtCore.QSize(1030, 701))
        Dialog.setMaximumSize(QtCore.QSize(1040, 701))
        Dialog.setBaseSize(QtCore.QSize(1030, 701))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(348, 157, 151, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("uisc/blank_2.png"))
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(185, 157, 151, 141))
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("uisc/blank_1.png"))
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 157, 151, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("uisc/blank_3.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(670, 157, 151, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("uisc/blank_4.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(180, 310, 121, 121))
        self.pushButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("uisc/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QtCore.QSize(140, 140))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 310, 121, 121))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("uisc/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 310, 121, 121))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("uisc/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 310, 121, 121))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("uisc/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(1155, 155))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 310, 121, 121))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("uisc/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 440, 121, 121))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("uisc/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 440, 121, 121))
        self.pushButton_7.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("uisc/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 440, 121, 121))
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("uisc/8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 440, 121, 121))
        self.pushButton_9.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("uisc/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.pushButton_0.setGeometry(QtCore.QRect(700, 440, 121, 121))
        self.pushButton_0.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("uisc/0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_0.setIcon(icon9)
        self.pushButton_0.setIconSize(QtCore.QSize(155, 155))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_arrow = QtWidgets.QPushButton(Dialog)
        self.pushButton_arrow.setGeometry(QtCore.QRect(180, 570, 251, 101))
        self.pushButton_arrow.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("uisc/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_arrow.setIcon(icon10)
        self.pushButton_arrow.setIconSize(QtCore.QSize(1555, 1555))
        self.pushButton_arrow.setObjectName("pushButton_arrow")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(440, 570, 371, 101))
        self.pushButton_search.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("uisc/검색.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon11)
        self.pushButton_search.setIconSize(QtCore.QSize(500, 500))
        self.pushButton_search.setObjectName("pushButton_search")
        self.label_maintitle = QtWidgets.QLabel(Dialog)
        self.label_maintitle.setGeometry(QtCore.QRect(303, 37, 371, 61))
        self.label_maintitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_maintitle.setText("")
        self.label_maintitle.setPixmap(QtGui.QPixmap("uisc/주차감면신청.png"))
        self.label_maintitle.setObjectName("label_maintitle")
        self.label_subtitle = QtWidgets.QLabel(Dialog)
        self.label_subtitle.setGeometry(QtCore.QRect(176, 100, 641, 51))
        self.label_subtitle.setText("")
        self.label_subtitle.setPixmap(QtGui.QPixmap("uisc/주차하신_차량의_차량번호_뒷자리(4자리)를_입력하세요.png"))
        self.label_subtitle.setObjectName("label_subtitle")
        self.box_1 = QtWidgets.QLabel(Dialog)
        self.box_1.setGeometry(QtCore.QRect(227, 178, 111, 111))
        font = QtGui.QFont()
        font.setFamily("a아시아고딕E")
        font.setPointSize(80)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.box_1.setFont(font)
        self.box_1.setMouseTracking(True)
        self.box_1.setAcceptDrops(False)
        self.box_1.setToolTipDuration(-1)
        self.box_1.setTextFormat(QtCore.Qt.RichText)
        self.box_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.box_1.setObjectName("box_1")
        self.box_2 = QtWidgets.QLabel(Dialog)
        self.box_2.setGeometry(QtCore.QRect(389, 178, 111, 111))
        font = QtGui.QFont()
        font.setFamily("a아시아고딕E")
        font.setPointSize(80)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.box_2.setFont(font)
        self.box_2.setMouseTracking(True)
        self.box_2.setAcceptDrops(False)
        self.box_2.setToolTipDuration(-1)
        self.box_2.setTextFormat(QtCore.Qt.RichText)
        self.box_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.box_2.setObjectName("box_2")
        self.box_3 = QtWidgets.QLabel(Dialog)
        self.box_3.setGeometry(QtCore.QRect(552, 178, 111, 111))
        font = QtGui.QFont()
        font.setFamily("a아시아고딕E")
        font.setPointSize(80)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.box_3.setFont(font)
        self.box_3.setMouseTracking(True)
        self.box_3.setAcceptDrops(False)
        self.box_3.setToolTipDuration(-1)
        self.box_3.setTextFormat(QtCore.Qt.RichText)
        self.box_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.box_3.setObjectName("box_3")
        self.box_4 = QtWidgets.QLabel(Dialog)
        self.box_4.setGeometry(QtCore.QRect(714, 178, 111, 111))
        font = QtGui.QFont()
        font.setFamily("a아시아고딕E")
        font.setPointSize(80)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.box_4.setFont(font)
        self.box_4.setMouseTracking(True)
        self.box_4.setAcceptDrops(False)
        self.box_4.setToolTipDuration(-1)
        self.box_4.setTextFormat(QtCore.Qt.RichText)
        self.box_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.box_4.setObjectName("box_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)





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
        

        
   

    

    def method_search(self):
        bbb=list(map(str,self.nlist))
        s="".join(bbb)
        test=cargo(s)
        test.start()
        self.box_1.setText("")
        self.box_2.setText("")
        self.box_3.setText("")
        self.box_4.setText("")

    def method_arrow(self):
        self.outnum()
        self.listdel()

    def method_1(self):
        self.innum(1)
        self.listinput()
        print(self.nlist)

    def method_2(self):
        self.innum(2)
        self.listinput()
        print(self.nlist)

    def method_3(self):
        self.innum(3)
        self.listinput()
        print(self.nlist)

    def method_4(self):
        self.innum(4)
        self.listinput()
        print(self.nlist)

    def method_5(self):
        self.innum(5)
        self.listinput()
        print(self.nlist)

    def method_6(self):
        self.innum(6)
        self.listinput()
        print(self.nlist)

    def method_7(self):
        self.innum(7)
        self.listinput()
        print(self.nlist)

    def method_8(self):
        self.innum(8)
        self.listinput()
        print(self.nlist)

    def method_9(self):
        self.innum(9)
        self.listinput()
        print(self.nlist)

    def method_0(self):
        self.innum(0)
        self.listinput()
        print(self.nlist)

    def listinput(self):
        if len(self.nlist)==1:
            self.box_1.setText(str(self.nlist[0]))
        elif len(self.nlist)==2:
            self.box_1.setText(str(self.nlist[0]))
            self.box_2.setText(str(self.nlist[1]))
        elif len(self.nlist)==3:
            self.box_1.setText(str(self.nlist[0]))
            self.box_2.setText(str(self.nlist[1]))
            self.box_3.setText(str(self.nlist[2]))
        elif len(self.nlist)==4:
            self.box_1.setText(str(self.nlist[0]))
            self.box_2.setText(str(self.nlist[1]))
            self.box_3.setText(str(self.nlist[2]))
            self.box_4.setText(str(self.nlist[3]))
        
    def listdel(self):
        if len(self.nlist)==0:
            self.box_1.setText("")
        elif len(self.nlist)==1:
            self.box_2.setText("")
        elif len(self.nlist)==2:
            self.box_3.setText("")
        elif len(self.nlist)==3:
            self.box_4.setText("")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.box_1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.box_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.box_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.box_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

