# This file installs a specific version of PyQt4 for Windows, as used by DrumBurp

Set-PSDebug -Trace 1
if (!(Test_Path pyqt_installer.exe -PathType Leaf)) {
    Invoke-WebRequest "https://netcologne.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.11.3/PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x64.exe" -OutFile pyqt_installer.exe
}
& ./pyqt_installer.exe /S