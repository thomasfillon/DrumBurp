'''
Created on 12 Dec 2010

@author: Mike Thomas
'''

#pylint:disable-msg=C0301

EMPTY_NOTE = "-"
BAR_TYPES = {"NO_BAR": 0,
             "NORMAL_BAR": 1,
             "REPEAT_START": 2,
             "REPEAT_END":4,
             "SECTION_END":8,
             "LINE_BREAK":16}
BARLINE = "|"
REPEAT_STARTER = BARLINE
REPEAT_END = BARLINE
REPEAT_EXTENDER = EMPTY_NOTE
