import sys
import Tutorial
from PyQt5 import QtWidgets
import ctypes

#check if the script run as administrator or not if not  it'll restart the script with admin rights
def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print ('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None

if __name__ == "__main__":
    run_as_admin()
    app = QtWidgets.QApplication(sys.argv)
    tutorial = Tutorial.tutorial_Form()
    tutorial.show()
    sys.exit(app.exec_())


