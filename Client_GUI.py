# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Icons_rc

class Ui_Form_client(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 774)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(51,51,51);")
        self.Master = QtWidgets.QTabWidget(Form)
        self.Master.setEnabled(True)
        self.Master.setGeometry(QtCore.QRect(20, 140, 971, 571))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Master.setFont(font)
        self.Master.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Master.setAcceptDrops(False)
        self.Master.setToolTip("")
        self.Master.setAutoFillBackground(False)
        self.Master.setStyleSheet("QWidget{\n"
"background-color: rgb(91,90,90);\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: rgb(51,51,51);\n"
" \n"
"} \n"
"QTabBar::tab:hover {\n"
"\n"
"background-color: rgb(68,85,90);\n"
" \n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"background-color: rgb(91,90,90);\n"
"\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"border:0px;\n"
"    \n"
"}")
        self.Master.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Master.setTabPosition(QtWidgets.QTabWidget.West)
        self.Master.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Master.setIconSize(QtCore.QSize(40, 40))
        self.Master.setElideMode(QtCore.Qt.ElideNone)
        self.Master.setUsesScrollButtons(True)
        self.Master.setObjectName("Master")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"    background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"       background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"    background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(10, 243, 141, 41))
        self.label_12.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255,255,255);")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(800, 520, 115, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(51,51,51);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 520, 115, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(51,51,51);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(330, 220, 271, 25))
        self.label_13.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(255,255,255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(350, 390, 151, 25))
        self.label_14.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:rgb(255,255,255);")
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 250, 121, 35))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_3.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(530, 390, 381, 25))
        self.label_17.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:rgb(255,255,255);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(350, 440, 151, 25))
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:rgb(255,255,255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(530, 440, 381, 25))
        self.label_19.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:rgb(255,255,255);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(150, 250, 611, 35))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    \n"
"    background:rgb(112,112,112);\n"
"    \n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"}")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lab_person_2 = QtWidgets.QLabel(self.tab)
        self.lab_person_2.setGeometry(QtCore.QRect(320, 0, 55, 55))
        self.lab_person_2.setMaximumSize(QtCore.QSize(55, 55))
        self.lab_person_2.setText("")
        self.lab_person_2.setPixmap(QtGui.QPixmap("../Minimalistic-Flat-Modern-GUI-Template-master/icons/1x/peple.png"))
        self.lab_person_2.setScaledContents(False)
        self.lab_person_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_person_2.setObjectName("lab_person_2")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(350, 330, 151, 25))
        self.label_21.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:rgb(255,255,255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(530, 330, 141, 25))
        self.label_22.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:rgb(255,255,255);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.lab_user_4 = QtWidgets.QLabel(self.tab)
        self.lab_user_4.setGeometry(QtCore.QRect(380, 0, 131, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lab_user_4.setFont(font)
        self.lab_user_4.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user_4.setObjectName("lab_user_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 10, 101, 38))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(51,51,51);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 164, 141, 41))
        self.label_23.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:rgb(255,255,255);")
        self.label_23.setObjectName("label_23")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 170, 611, 35))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    \n"
"    background:rgb(112,112,112);\n"
"    \n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 170, 121, 35))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_7.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(10, 80, 191, 25))
        self.label_24.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:rgb(255,255,255);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(340, 140, 391, 25))
        self.label_25.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:rgb(255,255,255);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(220, 80, 691, 25))
        self.label_26.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:rgb(255,255,255);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(210, 525, 511, 25))
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:rgb(255,255,255);")
        self.label_15.setObjectName("label_15")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Master.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tree_photo = QtWidgets.QLabel(self.tab_2)
        self.tree_photo.setGeometry(QtCore.QRect(30, 30, 861, 511))
        self.tree_photo.setText("")
        self.tree_photo.setObjectName("tree_photo")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/network.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Master.addTab(self.tab_2, icon1, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.statistics_photo = QtWidgets.QLabel(self.widget)
        self.statistics_photo.setGeometry(QtCore.QRect(30, 30, 861, 511))
        self.statistics_photo.setText("")
        self.statistics_photo.setObjectName("statistics_photo")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/statistic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Master.addTab(self.widget, icon2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 30, 811, 421))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    \n"
"    background:rgb(112,112,112);\n"
"    \n"
"}\n"
"\n"
"QPlainTextEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"}")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 480, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("QPlainTextEdit {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(51,51,51);\n"
"    border-radius:4px;\n"
"    \n"
"    background:rgb(112,112,112);\n"
"    \n"
"}\n"
"\n"
"QPlainTextEdit:disabled {\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid rgb(112,112,112);\n"
"    border-radius:4px;\n"
"    background:rgb(51,51,51);\n"
"}")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 480, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 480, 51, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(51,51,51);\n"
"    border-radius: 5px;    \n"
"    color:rgb(255,255,255);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    border: 2px solid rgb(0,143,150);\n"
"    background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {    \n"
"    border-radius: 5px;    \n"
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/Share.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_5.setObjectName("pushButton_5")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Master.addTab(self.tab_4, icon4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Master.addTab(self.tab_3, icon5, "")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(50, 60, 241, 51))
        self.label_20.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(255,255,255);")
        self.label_20.setObjectName("label_20")
        self.lab_user = QtWidgets.QLabel(Form)
        self.lab_user.setGeometry(QtCore.QRect(350, 0, 161, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.lab_user.setFont(font)
        self.lab_user.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user.setObjectName("lab_user")
        self.lab_user_2 = QtWidgets.QLabel(Form)
        self.lab_user_2.setGeometry(QtCore.QRect(530, 0, 201, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lab_user_2.setFont(font)
        self.lab_user_2.setStyleSheet("color:rgb(138, 11, 49);")
        self.lab_user_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user_2.setObjectName("lab_user_2")
        self.lab_user_3 = QtWidgets.QLabel(Form)
        self.lab_user_3.setGeometry(QtCore.QRect(730, 0, 131, 55))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lab_user_3.setFont(font)
        self.lab_user_3.setStyleSheet("color:rgb(255,255,255);")
        self.lab_user_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_user_3.setObjectName("lab_user_3")
        self.bn_close = QtWidgets.QPushButton(Form)
        self.bn_close.setGeometry(QtCore.QRect(992, 0, 55, 55))
        self.bn_close.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_close.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_close.setIcon(icon6)
        self.bn_close.setIconSize(QtCore.QSize(22, 22))
        self.bn_close.setFlat(True)
        self.bn_close.setObjectName("bn_close")
        self.bn_min = QtWidgets.QPushButton(Form)
        self.bn_min.setGeometry(QtCore.QRect(932, 0, 55, 55))
        self.bn_min.setMaximumSize(QtCore.QSize(55, 55))
        self.bn_min.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_min.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_min.setIcon(icon7)
        self.bn_min.setIconSize(QtCore.QSize(22, 22))
        self.bn_min.setFlat(True)
        self.bn_min.setObjectName("bn_min")
        self.lab_person = QtWidgets.QLabel(Form)
        self.lab_person.setGeometry(QtCore.QRect(870, 0, 55, 55))
        self.lab_person.setMaximumSize(QtCore.QSize(55, 55))
        self.lab_person.setText("")
        self.lab_person.setPixmap(QtGui.QPixmap(":/Icons/people.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_person.setObjectName("lab_person")

        self.retranslateUi(Form)
        self.Master.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox_2.setText(_translate("Form", "Show Password"))
        self.label_12.setText(_translate("Form", "Password          :"))
        self.pushButton.setText(_translate("Form", "Connect"))
        self.pushButton_2.setText(_translate("Form", "Disconnect"))
        self.label_13.setText(_translate("Form", "Password must be at least 8 characters"))
        self.label_14.setText(_translate("Form", "Connected To     :"))
        self.pushButton_3.setText(_translate("Form", "Change Password"))
        self.label_18.setText(_translate("Form", "My ID                  :"))
        self.label_21.setText(_translate("Form", "Status                  :"))
        self.lab_user_4.setText(_translate("Form", "<html><head/><body><p>    CLIENT</p></body></html>"))
        self.pushButton_6.setText(_translate("Form", "Change"))
        self.label_23.setText(_translate("Form", "Room Number :"))
        self.pushButton_7.setText(_translate("Form", "Change Room Number"))
        self.label_24.setText(_translate("Form", "Current Available Rooms :"))
        self.label_25.setText(_translate("Form", "You can choose not available room"))
        self.label_15.setText(_translate("Form", "                                     Press Start ..."))
        self.Master.setTabToolTip(self.Master.indexOf(self.tab), _translate("Form", "Configuration"))
        self.Master.setTabToolTip(self.Master.indexOf(self.tab_2), _translate("Form", "Network Hierarchy Structure"))
        self.Master.setTabToolTip(self.Master.indexOf(self.widget), _translate("Form", "Statistics"))
        self.pushButton_4.setText(_translate("Form", "Send"))
        self.Master.setTabToolTip(self.Master.indexOf(self.tab_4), _translate("Form", "Chat & Sharing Files"))
        self.label_20.setText(_translate("Form", "ChainSpoT"))
        self.lab_user.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lab_user_2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lab_user_3.setText(_translate("Form", "<html><head/><body><p>CLIENT</p></body></html>"))
        self.bn_close.setToolTip(_translate("Form", "Close"))
        self.bn_min.setToolTip(_translate("Form", "Minimize"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_client()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
