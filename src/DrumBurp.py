'''
Created on 31 Jul 2010

@author: Mike Thomas
'''
import sys
from PyQt4.QtGui import QApplication
import GUI.DBMainwindow
import GUI.DBIcons

def main():
    import ctypes
    myappid = 'Whatang.DrumBurp'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QApplication(sys.argv)
    app.setOrganizationName("Whatang Software")
    app.setOrganizationDomain("whatang.org")
    app.setApplicationName(GUI.DBMainwindow.APPNAME)
    mainWindow = GUI.DBMainwindow.DrumBurp()
    mainWindow.show()
    app.setWindowIcon(GUI.DBIcons.getIcon("drumburp"))
    app.exec_()

if __name__ == '__main__':
    main()
