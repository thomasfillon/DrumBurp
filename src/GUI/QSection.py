'''
Created on 26 Jan 2011

@author: Mike Thomas

'''

from PyQt4.QtGui import QGraphicsTextItem, QTextCursor
from PyQt4.QtCore import Qt
from DBCommands import SetSectionTitleCommand

class QSection(QGraphicsTextItem):
    '''
    classdocs
    '''


    def __init__(self, title, qScore = None, parent = None):
        '''
        Constructor
        '''
        super(QSection, self).__init__(parent = parent, scene = qScore)
        font = qScore.displayProperties.sectionFont
#        font = self.font()
        if font is None:
            font = self.font()
        font.setBold(True)
        font.setItalic(True)
        font.setPointSize(qScore.displayProperties.sectionFontSize)
        self.setFont(font)
        self.setTextInteractionFlags(Qt.TextEditable | Qt.TextSelectableByMouse)
        self._title = None
        self.setTitle(title)
        self._index = None
        self.setCursor(Qt.PointingHandCursor)

    def setIndex(self, index):
        self._index = index

    _keyMoves = {Qt.Key_Left:QTextCursor.Left,
                 Qt.Key_Right:QTextCursor.Right,
                 Qt.Key_Home:QTextCursor.Start,
                 Qt.Key_End:QTextCursor.End,
                 Qt.Key_Up:QTextCursor.NoMove,
                 Qt.Key_Down:QTextCursor.NoMove}
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()
            self.clearFocus()
        elif event.key() == Qt.Key_Escape:
            event.ignore()
            self.setPlainText(self._title)
            self.clearFocus()
        elif event.key() in self._keyMoves:
            cursor = self.textCursor()
            cursor.movePosition(self._keyMoves[event.key()])
            self.setTextCursor(cursor)
        else:
            super(QSection, self).keyPressEvent(event)

    def focusOutEvent(self, event):
        text = unicode(self.document().toPlainText())
        if text != self._title:
            self._title = text
            command = SetSectionTitleCommand(self.scene(),
                                             self._index,
                                             self._title)
            self.scene().addCommand(command)
        super(QSection, self).focusOutEvent(event)

    def setTitle(self, text):
        self._title = text
        self.setPlainText(text)
