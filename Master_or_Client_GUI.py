from PyQt5 import QtCore, QtGui, QtWidgets
import Icons_rc

class Ui_Form_master_or_client(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 565)
        Form.setStyleSheet("background-color: rgb(51,51,51);")
        self.bn_close = QtWidgets.QPushButton(Form)
        self.bn_close.setGeometry(QtCore.QRect(710, 0, 55, 55))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Minimalistic-Flat-Modern-GUI-Template-master/icons/1x/closeAsset 43.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_close.setIcon(icon)
        self.bn_close.setIconSize(QtCore.QSize(22, 22))
        self.bn_close.setFlat(True)
        self.bn_close.setObjectName("bn_close")
        self.bn_min = QtWidgets.QPushButton(Form)
        self.bn_min.setGeometry(QtCore.QRect(650, 0, 55, 55))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Minimalistic-Flat-Modern-GUI-Template-master/icons/1x/hideAsset 53.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QtCore.QSize(22, 22))
        self.bn_min.setFlat(True)
        self.bn_min.setObjectName("bn_min")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 671, 341))
        self.groupBox.setStyleSheet("background-color: rgb(91,90,90);\n"
"border:0px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 170, 150, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
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
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 170, 150, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton_5.setFont(font)
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(40, 30, 581, 61))
        self.label_20.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(33)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(255,255,255);")
        self.label_20.setObjectName("label_20")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 45, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
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
"    border: 2px solid rgb(112,112,112);\n"
"    background-color: rgb(112,112,112);\n"
"}")
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lab_person = QtWidgets.QLabel(Form)
        self.lab_person.setGeometry(QtCore.QRect(580, 0, 55, 55))
        self.lab_person.setMaximumSize(QtCore.QSize(55, 55))
        self.lab_person.setText("")
        self.lab_person.setPixmap(QtGui.QPixmap("../Minimalistic-Flat-Modern-GUI-Template-master/icons/1x/peple.png"))
        self.lab_person.setScaledContents(False)
        self.lab_person.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_person.setObjectName("lab_person")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(50, 60, 241, 51))
        self.label_21.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:rgb(255,255,255);")
        self.label_21.setObjectName("label_21")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bn_close.setToolTip(_translate("Form", "Close"))
        self.bn_min.setToolTip(_translate("Form", "Minimize"))
        self.pushButton_4.setText(_translate("Form", "Master"))
        self.pushButton_5.setText(_translate("Form", "Client"))
        self.label_20.setText(_translate("Form", "Are you Master or Client ?"))
        self.label_21.setText(_translate("Form", "ChainSpoT"))

