# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\drumburp.ui'
#
# Created: Sat Jan 08 16:31:10 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DrumBurpWindow(object):
    def setupUi(self, DrumBurpWindow):
        DrumBurpWindow.setObjectName(_fromUtf8("DrumBurpWindow"))
        DrumBurpWindow.resize(800, 600)
        DrumBurpWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(DrumBurpWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scoreView = ScoreView(self.centralwidget)
        self.scoreView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.scoreView.setAcceptDrops(False)
        self.scoreView.setLineWidth(1)
        self.scoreView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scoreView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.scoreView.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
        self.scoreView.setObjectName(_fromUtf8("scoreView"))
        self.gridLayout_2.addWidget(self.scoreView, 0, 0, 1, 1)
        DrumBurpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DrumBurpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuShow = QtGui.QMenu(self.menuView)
        self.menuShow.setObjectName(_fromUtf8("menuShow"))
        self.menuType_Here = QtGui.QMenu(self.menuView)
        self.menuType_Here.setObjectName(_fromUtf8("menuType_Here"))
        self.menuType_Here_2 = QtGui.QMenu(self.menuView)
        self.menuType_Here_2.setObjectName(_fromUtf8("menuType_Here_2"))
        DrumBurpWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DrumBurpWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DrumBurpWindow.setStatusBar(self.statusbar)
        self.fileToolBar = QtGui.QToolBar(DrumBurpWindow)
        self.fileToolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.fileToolBar.setMovable(True)
        self.fileToolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.fileToolBar.setObjectName(_fromUtf8("fileToolBar"))
        DrumBurpWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.fileToolBar)
        self.noteHeadDock = QtGui.QDockWidget(DrumBurpWindow)
        self.noteHeadDock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.noteHeadDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.noteHeadDock.setObjectName(_fromUtf8("noteHeadDock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.defaultNoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.defaultNoteHeadButton.setChecked(True)
        self.defaultNoteHeadButton.setObjectName(_fromUtf8("defaultNoteHeadButton"))
        self.gridLayout.addWidget(self.defaultNoteHeadButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.bigXNoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.bigXNoteHeadButton.setObjectName(_fromUtf8("bigXNoteHeadButton"))
        self.gridLayout.addWidget(self.bigXNoteHeadButton, 3, 1, 1, 1)
        self.xNoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.xNoteHeadButton.setObjectName(_fromUtf8("xNoteHeadButton"))
        self.gridLayout.addWidget(self.xNoteHeadButton, 3, 0, 1, 1)
        self.bigONoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.bigONoteHeadButton.setObjectName(_fromUtf8("bigONoteHeadButton"))
        self.gridLayout.addWidget(self.bigONoteHeadButton, 4, 1, 1, 1)
        self.oNoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.oNoteHeadButton.setObjectName(_fromUtf8("oNoteHeadButton"))
        self.gridLayout.addWidget(self.oNoteHeadButton, 4, 0, 1, 1)
        self.plusNoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.plusNoteHeadButton.setObjectName(_fromUtf8("plusNoteHeadButton"))
        self.gridLayout.addWidget(self.plusNoteHeadButton, 4, 2, 1, 1)
        self.gNoteHeadButton = RadioButtonTeller(self.dockWidgetContents)
        self.gNoteHeadButton.setObjectName(_fromUtf8("gNoteHeadButton"))
        self.gridLayout.addWidget(self.gNoteHeadButton, 3, 2, 1, 1)
        self.noteHeadDock.setWidget(self.dockWidgetContents)
        DrumBurpWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.noteHeadDock)
        self.diplayOptionsDock = QtGui.QDockWidget(DrumBurpWindow)
        self.diplayOptionsDock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.diplayOptionsDock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.diplayOptionsDock.setObjectName(_fromUtf8("diplayOptionsDock"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.spacingLabel = QtGui.QLabel(self.dockWidgetContents_2)
        self.spacingLabel.setWordWrap(True)
        self.spacingLabel.setObjectName(_fromUtf8("spacingLabel"))
        self.verticalLayout_2.addWidget(self.spacingLabel)
        self.spaceSlider = QtGui.QSlider(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spaceSlider.sizePolicy().hasHeightForWidth())
        self.spaceSlider.setSizePolicy(sizePolicy)
        self.spaceSlider.setMaximum(100)
        self.spaceSlider.setProperty(_fromUtf8("value"), 0)
        self.spaceSlider.setTracking(False)
        self.spaceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.spaceSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.spaceSlider.setObjectName(_fromUtf8("spaceSlider"))
        self.verticalLayout_2.addWidget(self.spaceSlider)
        self.label = QtGui.QLabel(self.dockWidgetContents_2)
        self.label.setToolTip(_fromUtf8(""))
        self.label.setStatusTip(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalSlider = QtGui.QSlider(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setTracking(False)
        self.verticalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.verticalLayout_2.addWidget(self.verticalSlider)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_2.setToolTip(_fromUtf8(""))
        self.label_2.setStatusTip(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineSpaceSlider = QtGui.QSlider(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSpaceSlider.sizePolicy().hasHeightForWidth())
        self.lineSpaceSlider.setSizePolicy(sizePolicy)
        self.lineSpaceSlider.setMaximum(100)
        self.lineSpaceSlider.setTracking(False)
        self.lineSpaceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lineSpaceSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.lineSpaceSlider.setObjectName(_fromUtf8("lineSpaceSlider"))
        self.verticalLayout_2.addWidget(self.lineSpaceSlider)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.widthSpinBox = QtGui.QSpinBox(self.dockWidgetContents_2)
        self.widthSpinBox.setMinimum(10)
        self.widthSpinBox.setMaximum(1000)
        self.widthSpinBox.setProperty(_fromUtf8("value"), 80)
        self.widthSpinBox.setObjectName(_fromUtf8("widthSpinBox"))
        self.horizontalLayout_2.addWidget(self.widthSpinBox)
        self.fitWindowButton = QtGui.QPushButton(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitWindowButton.sizePolicy().hasHeightForWidth())
        self.fitWindowButton.setSizePolicy(sizePolicy)
        self.fitWindowButton.setObjectName(_fromUtf8("fitWindowButton"))
        self.horizontalLayout_2.addWidget(self.fitWindowButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widthLabel = QtGui.QLabel(self.dockWidgetContents_2)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.verticalLayout_2.addWidget(self.widthLabel)
        self.fontComboBox = QtGui.QFontComboBox(self.dockWidgetContents_2)
        self.fontComboBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setMinimumSize(QtCore.QSize(100, 20))
        self.fontComboBox.setMaximumSize(QtCore.QSize(187, 20))
        self.fontComboBox.setEditable(False)
        self.fontComboBox.setMaxVisibleItems(20)
        self.fontComboBox.setFontFilters(QtGui.QFontComboBox.ScalableFonts)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("BatangChe"))
        font.setPointSize(10)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.verticalLayout_2.addWidget(self.fontComboBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.diplayOptionsDock.setWidget(self.dockWidgetContents_2)
        DrumBurpWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.diplayOptionsDock)
        self.songPropertiesDock = QtGui.QDockWidget(DrumBurpWindow)
        self.songPropertiesDock.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.songPropertiesDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.songPropertiesDock.setObjectName(_fromUtf8("songPropertiesDock"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.songNameLabel = QtGui.QLabel(self.dockWidgetContents_3)
        self.songNameLabel.setObjectName(_fromUtf8("songNameLabel"))
        self.gridLayout_3.addWidget(self.songNameLabel, 0, 0, 1, 1)
        self.songNameEdit = QtGui.QLineEdit(self.dockWidgetContents_3)
        self.songNameEdit.setObjectName(_fromUtf8("songNameEdit"))
        self.gridLayout_3.addWidget(self.songNameEdit, 0, 1, 1, 1)
        self.artistNameEdit = QtGui.QLineEdit(self.dockWidgetContents_3)
        self.artistNameEdit.setObjectName(_fromUtf8("artistNameEdit"))
        self.gridLayout_3.addWidget(self.artistNameEdit, 2, 1, 1, 1)
        self.tabberLabel = QtGui.QLabel(self.dockWidgetContents_3)
        self.tabberLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.tabberLabel.setObjectName(_fromUtf8("tabberLabel"))
        self.gridLayout_3.addWidget(self.tabberLabel, 2, 3, 1, 1)
        self.tabberEdit = QtGui.QLineEdit(self.dockWidgetContents_3)
        self.tabberEdit.setObjectName(_fromUtf8("tabberEdit"))
        self.gridLayout_3.addWidget(self.tabberEdit, 2, 4, 1, 1)
        self.artistNameLabel = QtGui.QLabel(self.dockWidgetContents_3)
        self.artistNameLabel.setObjectName(_fromUtf8("artistNameLabel"))
        self.gridLayout_3.addWidget(self.artistNameLabel, 2, 0, 1, 1)
        self.bpmLabel = QtGui.QLabel(self.dockWidgetContents_3)
        self.bpmLabel.setObjectName(_fromUtf8("bpmLabel"))
        self.gridLayout_3.addWidget(self.bpmLabel, 0, 3, 1, 1)
        self.bpmSpinBox = QtGui.QSpinBox(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bpmSpinBox.sizePolicy().hasHeightForWidth())
        self.bpmSpinBox.setSizePolicy(sizePolicy)
        self.bpmSpinBox.setMaximum(300)
        self.bpmSpinBox.setProperty(_fromUtf8("value"), 120)
        self.bpmSpinBox.setObjectName(_fromUtf8("bpmSpinBox"))
        self.gridLayout_3.addWidget(self.bpmSpinBox, 0, 4, 1, 1)
        self.songPropertiesDock.setWidget(self.dockWidgetContents_3)
        DrumBurpWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.songPropertiesDock)
        self.viewToolBar = QtGui.QToolBar(DrumBurpWindow)
        self.viewToolBar.setMovable(True)
        self.viewToolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.viewToolBar.setObjectName(_fromUtf8("viewToolBar"))
        DrumBurpWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.viewToolBar)
        self.actionQuit = QtGui.QAction(DrumBurpWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionNew = QtGui.QAction(DrumBurpWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionLoad = QtGui.QAction(DrumBurpWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(DrumBurpWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(DrumBurpWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionExport_ASCII = QtGui.QAction(DrumBurpWindow)
        self.actionExport_ASCII.setObjectName(_fromUtf8("actionExport_ASCII"))
        self.actionDisplayOptionsIsVisible = QtGui.QAction(DrumBurpWindow)
        self.actionDisplayOptionsIsVisible.setCheckable(True)
        self.actionDisplayOptionsIsVisible.setObjectName(_fromUtf8("actionDisplayOptionsIsVisible"))
        self.actionSongPropertiesIsVisible = QtGui.QAction(DrumBurpWindow)
        self.actionSongPropertiesIsVisible.setCheckable(True)
        self.actionSongPropertiesIsVisible.setObjectName(_fromUtf8("actionSongPropertiesIsVisible"))
        self.actionNoteHeadSelectorIsVisble = QtGui.QAction(DrumBurpWindow)
        self.actionNoteHeadSelectorIsVisble.setCheckable(True)
        self.actionNoteHeadSelectorIsVisble.setObjectName(_fromUtf8("actionNoteHeadSelectorIsVisble"))
        self.actionFileToolbarIsVisible = QtGui.QAction(DrumBurpWindow)
        self.actionFileToolbarIsVisible.setCheckable(True)
        self.actionFileToolbarIsVisible.setObjectName(_fromUtf8("actionFileToolbarIsVisible"))
        self.actionFitInWindow = QtGui.QAction(DrumBurpWindow)
        self.actionFitInWindow.setObjectName(_fromUtf8("actionFitInWindow"))
        self.actionToolbars = QtGui.QAction(DrumBurpWindow)
        self.actionToolbars.setObjectName(_fromUtf8("actionToolbars"))
        self.actionViewToolBarIsVisible = QtGui.QAction(DrumBurpWindow)
        self.actionViewToolBarIsVisible.setCheckable(True)
        self.actionViewToolBarIsVisible.setObjectName(_fromUtf8("actionViewToolBarIsVisible"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_ASCII)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuShow.addAction(self.actionDisplayOptionsIsVisible)
        self.menuShow.addAction(self.actionSongPropertiesIsVisible)
        self.menuShow.addAction(self.actionNoteHeadSelectorIsVisble)
        self.menuType_Here.addAction(self.actionFileToolbarIsVisible)
        self.menuType_Here.addAction(self.actionViewToolBarIsVisible)
        self.menuView.addAction(self.actionFitInWindow)
        self.menuView.addAction(self.menuShow.menuAction())
        self.menuView.addAction(self.menuType_Here.menuAction())
        self.menuView.addAction(self.menuType_Here_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.fileToolBar.addAction(self.actionNew)
        self.fileToolBar.addAction(self.actionLoad)
        self.fileToolBar.addAction(self.actionSave)
        self.fileToolBar.addAction(self.actionSave_As)
        self.fileToolBar.addAction(self.actionExport_ASCII)
        self.viewToolBar.addAction(self.actionFitInWindow)
        self.spacingLabel.setBuddy(self.spaceSlider)
        self.label.setBuddy(self.verticalSlider)
        self.label_2.setBuddy(self.lineSpaceSlider)
        self.label_3.setBuddy(self.widthSpinBox)
        self.widthLabel.setBuddy(self.fontComboBox)
        self.songNameLabel.setBuddy(self.songNameEdit)
        self.tabberLabel.setBuddy(self.tabberEdit)
        self.artistNameLabel.setBuddy(self.artistNameEdit)
        self.bpmLabel.setBuddy(self.bpmSpinBox)

        self.retranslateUi(DrumBurpWindow)
        QtCore.QObject.connect(self.defaultNoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.xNoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.bigXNoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.oNoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.bigONoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.plusNoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.gNoteHeadButton, QtCore.SIGNAL(_fromUtf8("emitValue(QString)")), self.scoreView.setNoteHead)
        QtCore.QObject.connect(self.spaceSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.scoreView.horizontalSpacingChanged)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.scoreView.verticalSpacingChanged)
        QtCore.QObject.connect(self.lineSpaceSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.scoreView.systemSpacingChanged)
        QtCore.QObject.connect(self.fontComboBox, QtCore.SIGNAL(_fromUtf8("currentFontChanged(QFont)")), self.scoreView.setFont)
        QtCore.QObject.connect(self.actionDisplayOptionsIsVisible, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.diplayOptionsDock.setVisible)
        QtCore.QObject.connect(self.actionNoteHeadSelectorIsVisble, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.noteHeadDock.setVisible)
        QtCore.QObject.connect(self.actionSongPropertiesIsVisible, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.songPropertiesDock.setVisible)
        QtCore.QObject.connect(self.songPropertiesDock, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionSongPropertiesIsVisible.setChecked)
        QtCore.QObject.connect(self.noteHeadDock, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionNoteHeadSelectorIsVisble.setChecked)
        QtCore.QObject.connect(self.diplayOptionsDock, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionDisplayOptionsIsVisible.setChecked)
        QtCore.QObject.connect(self.actionFileToolbarIsVisible, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.fileToolBar.setVisible)
        QtCore.QObject.connect(self.fileToolBar, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionFileToolbarIsVisible.setChecked)
        QtCore.QObject.connect(self.widthSpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.scoreView.setWidth)
        QtCore.QObject.connect(self.fitWindowButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionFitInWindow.trigger)
        QtCore.QObject.connect(self.viewToolBar, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.actionViewToolBarIsVisible.setChecked)
        QtCore.QObject.connect(self.actionViewToolBarIsVisible, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.viewToolBar.setVisible)
        QtCore.QMetaObject.connectSlotsByName(DrumBurpWindow)

    def retranslateUi(self, DrumBurpWindow):
        DrumBurpWindow.setWindowTitle(QtGui.QApplication.translate("DrumBurpWindow", "DrumBurp", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Operations on the DrumBurp Score", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("DrumBurpWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Options affecting the view", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("DrumBurpWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuShow.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Select visible components", None, QtGui.QApplication.UnicodeUTF8))
        self.menuShow.setTitle(QtGui.QApplication.translate("DrumBurpWindow", "Show...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuType_Here.setTitle(QtGui.QApplication.translate("DrumBurpWindow", "Show Tool Bars...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuType_Here_2.setTitle(QtGui.QApplication.translate("DrumBurpWindow", "Type Here", None, QtGui.QApplication.UnicodeUTF8))
        self.fileToolBar.setWindowTitle(QtGui.QApplication.translate("DrumBurpWindow", "File Tool Bar", None, QtGui.QApplication.UnicodeUTF8))
        self.noteHeadDock.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Select the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.noteHeadDock.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "The note head determines what note will be placed in the Score", None, QtGui.QApplication.UnicodeUTF8))
        self.noteHeadDock.setWindowTitle(QtGui.QApplication.translate("DrumBurpWindow", "Note Head", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultNoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Default note head", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultNoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use the default note head for each instrument", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultNoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.bigXNoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "X note head", None, QtGui.QApplication.UnicodeUTF8))
        self.bigXNoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use \"X\" as the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.bigXNoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.bigXNoteHeadButton.setProperty(_fromUtf8("buttonValue"), QtGui.QApplication.translate("DrumBurpWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.xNoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "x note head", None, QtGui.QApplication.UnicodeUTF8))
        self.xNoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use \"x\" as the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.xNoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.xNoteHeadButton.setProperty(_fromUtf8("buttonValue"), QtGui.QApplication.translate("DrumBurpWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.bigONoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "O note head", None, QtGui.QApplication.UnicodeUTF8))
        self.bigONoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use \"O\" as the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.bigONoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.bigONoteHeadButton.setProperty(_fromUtf8("buttonValue"), QtGui.QApplication.translate("DrumBurpWindow", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.oNoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "o note head", None, QtGui.QApplication.UnicodeUTF8))
        self.oNoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use \"o\" as the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.oNoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "o", None, QtGui.QApplication.UnicodeUTF8))
        self.oNoteHeadButton.setProperty(_fromUtf8("buttonValue"), QtGui.QApplication.translate("DrumBurpWindow", "o", None, QtGui.QApplication.UnicodeUTF8))
        self.plusNoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "+ note head", None, QtGui.QApplication.UnicodeUTF8))
        self.plusNoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use \"+\" as the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.plusNoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.plusNoteHeadButton.setProperty(_fromUtf8("buttonValue"), QtGui.QApplication.translate("DrumBurpWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.gNoteHeadButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "g note head", None, QtGui.QApplication.UnicodeUTF8))
        self.gNoteHeadButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Use \"g\" as the note head", None, QtGui.QApplication.UnicodeUTF8))
        self.gNoteHeadButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "g", None, QtGui.QApplication.UnicodeUTF8))
        self.gNoteHeadButton.setProperty(_fromUtf8("buttonValue"), QtGui.QApplication.translate("DrumBurpWindow", "g", None, QtGui.QApplication.UnicodeUTF8))
        self.diplayOptionsDock.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Display Options", None, QtGui.QApplication.UnicodeUTF8))
        self.diplayOptionsDock.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Options affecting how the Score is displayed", None, QtGui.QApplication.UnicodeUTF8))
        self.diplayOptionsDock.setWindowTitle(QtGui.QApplication.translate("DrumBurpWindow", "Display Options", None, QtGui.QApplication.UnicodeUTF8))
        self.spacingLabel.setText(QtGui.QApplication.translate("DrumBurpWindow", "Horizontal Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.spaceSlider.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Note width", None, QtGui.QApplication.UnicodeUTF8))
        self.spaceSlider.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "The width of each note in the Score", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DrumBurpWindow", "Vertical Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSlider.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Note height", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSlider.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "The height of each note in the Score", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DrumBurpWindow", "System Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.lineSpaceSlider.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Inter-system distance", None, QtGui.QApplication.UnicodeUTF8))
        self.lineSpaceSlider.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "The distance between each system in the Score", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DrumBurpWindow", "Columns:", None, QtGui.QApplication.UnicodeUTF8))
        self.widthSpinBox.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Score width", None, QtGui.QApplication.UnicodeUTF8))
        self.widthSpinBox.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "The number of columns to display the Score on", None, QtGui.QApplication.UnicodeUTF8))
        self.fitWindowButton.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Fit Score In Window", None, QtGui.QApplication.UnicodeUTF8))
        self.fitWindowButton.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Attempt to make the score as wide as possible within the current window.", None, QtGui.QApplication.UnicodeUTF8))
        self.fitWindowButton.setText(QtGui.QApplication.translate("DrumBurpWindow", "Fit Window", None, QtGui.QApplication.UnicodeUTF8))
        self.widthLabel.setText(QtGui.QApplication.translate("DrumBurpWindow", "Display font", None, QtGui.QApplication.UnicodeUTF8))
        self.fontComboBox.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "The font used to display notes in the Score", None, QtGui.QApplication.UnicodeUTF8))
        self.songPropertiesDock.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Song Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.songPropertiesDock.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Information about the Score", None, QtGui.QApplication.UnicodeUTF8))
        self.songPropertiesDock.setWindowTitle(QtGui.QApplication.translate("DrumBurpWindow", "Song Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.songNameLabel.setText(QtGui.QApplication.translate("DrumBurpWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.songNameEdit.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Song name", None, QtGui.QApplication.UnicodeUTF8))
        self.songNameEdit.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Song name", None, QtGui.QApplication.UnicodeUTF8))
        self.artistNameEdit.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Song artist", None, QtGui.QApplication.UnicodeUTF8))
        self.artistNameEdit.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Song artist", None, QtGui.QApplication.UnicodeUTF8))
        self.tabberLabel.setText(QtGui.QApplication.translate("DrumBurpWindow", "Created by", None, QtGui.QApplication.UnicodeUTF8))
        self.tabberEdit.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Score creator", None, QtGui.QApplication.UnicodeUTF8))
        self.tabberEdit.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Who created this DrumBurp score", None, QtGui.QApplication.UnicodeUTF8))
        self.artistNameLabel.setText(QtGui.QApplication.translate("DrumBurpWindow", "&Artist", None, QtGui.QApplication.UnicodeUTF8))
        self.bpmLabel.setText(QtGui.QApplication.translate("DrumBurpWindow", "&BPM", None, QtGui.QApplication.UnicodeUTF8))
        self.bpmSpinBox.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "BPM", None, QtGui.QApplication.UnicodeUTF8))
        self.bpmSpinBox.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Beats per minute", None, QtGui.QApplication.UnicodeUTF8))
        self.bpmSpinBox.setSuffix(QtGui.QApplication.translate("DrumBurpWindow", " bpm", None, QtGui.QApplication.UnicodeUTF8))
        self.viewToolBar.setWindowTitle(QtGui.QApplication.translate("DrumBurpWindow", "View Tool Bar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("DrumBurpWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Quit DrumBurp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Quit DrumBurp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("DrumBurpWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setIconText(QtGui.QApplication.translate("DrumBurpWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "New Score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Create a new blank score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("DrumBurpWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("DrumBurpWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Load Score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Load a saved DrumBurp score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setShortcut(QtGui.QApplication.translate("DrumBurpWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("DrumBurpWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Save this DrumBurp score", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("DrumBurpWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("DrumBurpWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Save this DrumBurp score with a new name", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_ASCII.setText(QtGui.QApplication.translate("DrumBurpWindow", "&Export ASCII", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_ASCII.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Write an ASCII representation of this score to a file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_ASCII.setShortcut(QtGui.QApplication.translate("DrumBurpWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplayOptionsIsVisible.setText(QtGui.QApplication.translate("DrumBurpWindow", "Display Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplayOptionsIsVisible.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of display options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisplayOptionsIsVisible.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of display options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSongPropertiesIsVisible.setText(QtGui.QApplication.translate("DrumBurpWindow", "Song Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSongPropertiesIsVisible.setIconText(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of song properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSongPropertiesIsVisible.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of song properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNoteHeadSelectorIsVisble.setText(QtGui.QApplication.translate("DrumBurpWindow", "Note Head Selector", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNoteHeadSelectorIsVisble.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of note head selector", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNoteHeadSelectorIsVisble.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of note head selector", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileToolbarIsVisible.setText(QtGui.QApplication.translate("DrumBurpWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileToolbarIsVisible.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of File tool bar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFileToolbarIsVisible.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of tool bar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFitInWindow.setText(QtGui.QApplication.translate("DrumBurpWindow", "Fit Window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFitInWindow.setStatusTip(QtGui.QApplication.translate("DrumBurpWindow", "Attempt to make the score as wide as possible within the current window.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToolbars.setText(QtGui.QApplication.translate("DrumBurpWindow", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewToolBarIsVisible.setText(QtGui.QApplication.translate("DrumBurpWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewToolBarIsVisible.setToolTip(QtGui.QApplication.translate("DrumBurpWindow", "Change visibility of View tool bar", None, QtGui.QApplication.UnicodeUTF8))

from Widgets.ScoreView_plugin import ScoreView
from Widgets.RadioButtonTeller_plugin import RadioButtonTeller