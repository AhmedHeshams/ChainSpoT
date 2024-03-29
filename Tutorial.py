# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tutorial.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint 
import Master_or_Client
import Tutorial_GUI
import sys

class tutorial_Form(QtWidgets.QWidget, Tutorial_GUI.Ui_Form_tutorial):
    def __init__(self, parent=None):
        super(tutorial_Form, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        #Center the window
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        self.setWindowTitle("ChainSpoT")
        self.setWindowIcon(QtGui.QIcon("Icons/logo.png"))
        self.oldPos = self.pos()
        self.setWindowFlag(Qt.FramelessWindowHint) #Hide the title bar of window
        self.pushButton_6.clicked.connect(self.skip)
        self.bn_close_2.clicked.connect(self.exit)
        self.bn_min_2.clicked.connect(self.showMinimized)
        self.tut_list=['''Hello! Welcome to our Chain.
A programm which enable you and your group to communite, chat and share files, without any infrastructure devices, just your laptop. ''',
 '''If you want to join Existing Room(network), Choose the client option in the main window, enter the room number & passord, press the join butoon and you are ready to go ''',
 '''If you and your group is ready to chat or share files, all you need to do is stablish a network. To do so choose the Master option in the main page , enter your password(not necessary) and press start button. doing this , your Room (network) now stablished with a number givin to you by the program. To strat chatting & sharing inform your group about the room number and password. They will now join your Room as a Client '''
 ]
        self.pushButton_4.hide()
        self.label.hide()
        self.pushButton_5.setText("Start")
        self.lab_home_main_disc.setFont(QtGui.QFont('Arial', 18))
        self.index = 0
        self.lab_home_main_disc.setText(self.tut_list[self.index])
        self.pushButton_5.clicked.connect(self.next)
        self.pushButton_4.clicked.connect(self.prev) 

    def exit(self):
        self.close()

    def next(self):
        if self.pushButton_5.text() == "Start":
            self.pushButton_5.setText("Next")
            self.pushButton_4.show()
            self.label.show()
            self.pushButton_4.setEnabled(True)
            self.index+=1
            self.lab_home_main_disc.setText(self.tut_list[self.index])
        elif(self.index<len(self.tut_list)-1):
            self.index+=1
            self.lab_home_main_disc.setText(self.tut_list[self.index])
            if (self.index == len(self.tut_list)-1):
                self.pushButton_5.setText("Finish")
        elif(self.index == len(self.tut_list)-1):
            self.skip()
            

    def prev(self):
        if (self.index > 0):
            self.index-=1
            self.lab_home_main_disc.setText(self.tut_list[self.index])
            if (self.index ==0):
                self.pushButton_4.setEnabled(False)
                self.pushButton_5.setText("Start")

        
    def skip(self):
        try:
            self.w = Master_or_Client.master_or_client_Form()
            self.w.show()
            self.close()
        except Exception as e:
            with open("general_error.txt","a") as f:
                f.write("from Tutrial "+str(e)+"\n")
        
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tutorial = tutorial_Form()
    tutorial.show()
    sys.exit(app.exec_())