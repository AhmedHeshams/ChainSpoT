In CMD write the next commands:
pip install PyQt5
pip install pyqt5-tools
if you have error with pyqt5-tools make sure you have python 3.9.10 

to transfer from ui to py write the next command in CMD:
pyuic5 -x filename.ui -o filename.py

to transfer from qrc to py write the next command in CMD:
pyrcc5 -o filename.py filename.qrc