# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StationQueryDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StationQueryDialog(object):
    def setupUi(self, StationQueryDialog):
        StationQueryDialog.setObjectName(_fromUtf8("StationQueryDialog"))
        StationQueryDialog.resize(550, 625)
        StationQueryDialog.setMinimumSize(QtCore.QSize(450, 0))
        self.verticalLayout = QtGui.QVBoxLayout(StationQueryDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.SNCLGroupBox = QtGui.QGroupBox(StationQueryDialog)
        self.SNCLGroupBox.setObjectName(_fromUtf8("SNCLGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.SNCLGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.locationLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.locationLabel.setObjectName(_fromUtf8("locationLabel"))
        self.gridLayout.addWidget(self.locationLabel, 0, 2, 1, 1)
        self.networkLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.networkLabel.setObjectName(_fromUtf8("networkLabel"))
        self.gridLayout.addWidget(self.networkLabel, 0, 0, 1, 1)
        self.channelLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.channelLabel.setObjectName(_fromUtf8("channelLabel"))
        self.gridLayout.addWidget(self.channelLabel, 0, 3, 1, 1)
        self.stationLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.stationLabel.setObjectName(_fromUtf8("stationLabel"))
        self.gridLayout.addWidget(self.stationLabel, 0, 1, 1, 1)
        self.stationLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.stationLineEdit.setObjectName(_fromUtf8("stationLineEdit"))
        self.gridLayout.addWidget(self.stationLineEdit, 1, 1, 1, 1)
        self.networkLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.networkLineEdit.setObjectName(_fromUtf8("networkLineEdit"))
        self.gridLayout.addWidget(self.networkLineEdit, 1, 0, 1, 1)
        self.locationLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.locationLineEdit.setObjectName(_fromUtf8("locationLineEdit"))
        self.gridLayout.addWidget(self.locationLineEdit, 1, 2, 1, 1)
        self.channelLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.channelLineEdit.setObjectName(_fromUtf8("channelLineEdit"))
        self.gridLayout.addWidget(self.channelLineEdit, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.SNCLGroupBox)
        self.timeGroupBox = QtGui.QGroupBox(StationQueryDialog)
        self.timeGroupBox.setObjectName(_fromUtf8("timeGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.timeGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.timeBetweenRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeBetweenRadioButton.setEnabled(True)
        self.timeBetweenRadioButton.setChecked(True)
        self.timeBetweenRadioButton.setObjectName(_fromUtf8("timeBetweenRadioButton"))
        self.verticalLayout_2.addWidget(self.timeBetweenRadioButton)
        self.timeWidget = QtGui.QWidget(self.timeGroupBox)
        self.timeWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.timeWidget.setObjectName(_fromUtf8("timeWidget"))
        self.endtimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeWidget)
        self.endtimeDateTimeEdit.setGeometry(QtCore.QRect(300, 12, 144, 24))
        self.endtimeDateTimeEdit.setObjectName(_fromUtf8("endtimeDateTimeEdit"))
        self.starttimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeWidget)
        self.starttimeDateTimeEdit.setGeometry(QtCore.QRect(70, 12, 160, 24))
        self.starttimeDateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starttimeDateTimeEdit.setObjectName(_fromUtf8("starttimeDateTimeEdit"))
        self.starttimeLabel = QtGui.QLabel(self.timeWidget)
        self.starttimeLabel.setGeometry(QtCore.QRect(25, 12, 40, 16))
        self.starttimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.starttimeLabel.setObjectName(_fromUtf8("starttimeLabel"))
        self.endtimeLabele = QtGui.QLabel(self.timeWidget)
        self.endtimeLabele.setGeometry(QtCore.QRect(255, 12, 40, 16))
        self.endtimeLabele.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endtimeLabele.setObjectName(_fromUtf8("endtimeLabele"))
        self.verticalLayout_2.addWidget(self.timeWidget)
        self.timeDuringEventsRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeDuringEventsRadioButton.setObjectName(_fromUtf8("timeDuringEventsRadioButton"))
        self.verticalLayout_2.addWidget(self.timeDuringEventsRadioButton)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.locationGroupBox = QtGui.QGroupBox(StationQueryDialog)
        self.locationGroupBox.setMinimumSize(QtCore.QSize(0, 375))
        self.locationGroupBox.setObjectName(_fromUtf8("locationGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.locationRangeRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationRangeRadioButton.setChecked(True)
        self.locationRangeRadioButton.setObjectName(_fromUtf8("locationRangeRadioButton"))
        self.verticalLayout_4.addWidget(self.locationRangeRadioButton)
        self.locationRangeWidget = QtGui.QWidget(self.locationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationRangeWidget.sizePolicy().hasHeightForWidth())
        self.locationRangeWidget.setSizePolicy(sizePolicy)
        self.locationRangeWidget.setMinimumSize(QtCore.QSize(0, 120))
        self.locationRangeWidget.setObjectName(_fromUtf8("locationRangeWidget"))
        self.locationRangeEastLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeEastLineEdit.setGeometry(QtCore.QRect(90, 40, 60, 21))
        self.locationRangeEastLineEdit.setObjectName(_fromUtf8("locationRangeEastLineEdit"))
        self.locationRangeWestLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeWestLineEdit.setGeometry(QtCore.QRect(20, 40, 60, 21))
        self.locationRangeWestLineEdit.setObjectName(_fromUtf8("locationRangeWestLineEdit"))
        self.locationRangeNorthLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeNorthLineEdit.setGeometry(QtCore.QRect(60, 12, 60, 21))
        self.locationRangeNorthLineEdit.setObjectName(_fromUtf8("locationRangeNorthLineEdit"))
        self.locationRangeSouthLineEdit = QtGui.QLineEdit(self.locationRangeWidget)
        self.locationRangeSouthLineEdit.setGeometry(QtCore.QRect(60, 70, 60, 21))
        self.locationRangeSouthLineEdit.setObjectName(_fromUtf8("locationRangeSouthLineEdit"))
        self.verticalLayout_4.addWidget(self.locationRangeWidget)
        self.locationDistanceFromPointRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromPointRadioButton.setEnabled(True)
        self.locationDistanceFromPointRadioButton.setObjectName(_fromUtf8("locationDistanceFromPointRadioButton"))
        self.verticalLayout_4.addWidget(self.locationDistanceFromPointRadioButton)
        self.distanceFromPointWidget = QtGui.QWidget(self.locationGroupBox)
        self.distanceFromPointWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.distanceFromPointWidget.setObjectName(_fromUtf8("distanceFromPointWidget"))
        self.distanceFromPointEastLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointEastLineEdit.setEnabled(True)
        self.distanceFromPointEastLineEdit.setGeometry(QtCore.QRect(70, 40, 60, 21))
        self.distanceFromPointEastLineEdit.setObjectName(_fromUtf8("distanceFromPointEastLineEdit"))
        self.label_8 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(135, 40, 10, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(225, 40, 10, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.distanceFromPointMinRadiusLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointMinRadiusLineEdit.setEnabled(True)
        self.distanceFromPointMinRadiusLineEdit.setGeometry(QtCore.QRect(20, 10, 60, 21))
        self.distanceFromPointMinRadiusLineEdit.setObjectName(_fromUtf8("distanceFromPointMinRadiusLineEdit"))
        self.label_10 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(85, 10, 10, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.distanceFromPointMaxRadiusLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointMaxRadiusLineEdit.setEnabled(True)
        self.distanceFromPointMaxRadiusLineEdit.setGeometry(QtCore.QRect(100, 10, 60, 21))
        self.distanceFromPointMaxRadiusLineEdit.setObjectName(_fromUtf8("distanceFromPointMaxRadiusLineEdit"))
        self.distanceFromPointNorthLineEdit = QtGui.QLineEdit(self.distanceFromPointWidget)
        self.distanceFromPointNorthLineEdit.setEnabled(True)
        self.distanceFromPointNorthLineEdit.setGeometry(QtCore.QRect(160, 40, 60, 21))
        self.distanceFromPointNorthLineEdit.setObjectName(_fromUtf8("distanceFromPointNorthLineEdit"))
        self.label_11 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(165, 10, 60, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_6 = QtGui.QLabel(self.distanceFromPointWidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 40, 13))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_10.raise_()
        self.distanceFromPointMaxRadiusLineEdit.raise_()
        self.distanceFromPointMinRadiusLineEdit.raise_()
        self.label_11.raise_()
        self.distanceFromPointEastLineEdit.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.distanceFromPointNorthLineEdit.raise_()
        self.label_6.raise_()
        self.verticalLayout_4.addWidget(self.distanceFromPointWidget)
        self.locationDistanceFromEventsRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromEventsRadioButton.setEnabled(False)
        self.locationDistanceFromEventsRadioButton.setObjectName(_fromUtf8("locationDistanceFromEventsRadioButton"))
        self.verticalLayout_4.addWidget(self.locationDistanceFromEventsRadioButton)
        self.distanceFromEventsWidget = QtGui.QWidget(self.locationGroupBox)
        self.distanceFromEventsWidget.setMinimumSize(QtCore.QSize(0, 45))
        self.distanceFromEventsWidget.setObjectName(_fromUtf8("distanceFromEventsWidget"))
        self.distanceFromEventsMinradiusLineEdit = QtGui.QLineEdit(self.distanceFromEventsWidget)
        self.distanceFromEventsMinradiusLineEdit.setEnabled(False)
        self.distanceFromEventsMinradiusLineEdit.setGeometry(QtCore.QRect(20, 12, 60, 21))
        self.distanceFromEventsMinradiusLineEdit.setObjectName(_fromUtf8("distanceFromEventsMinradiusLineEdit"))
        self.label_3 = QtGui.QLabel(self.distanceFromEventsWidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(85, 12, 10, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.distanceFromEventsMaxradiusLineEdit = QtGui.QLineEdit(self.distanceFromEventsWidget)
        self.distanceFromEventsMaxradiusLineEdit.setEnabled(False)
        self.distanceFromEventsMaxradiusLineEdit.setGeometry(QtCore.QRect(100, 12, 60, 21))
        self.distanceFromEventsMaxradiusLineEdit.setObjectName(_fromUtf8("distanceFromEventsMaxradiusLineEdit"))
        self.label_5 = QtGui.QLabel(self.distanceFromEventsWidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(165, 12, 60, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.distanceFromEventsWidget)
        self.verticalLayout.addWidget(self.locationGroupBox)

        self.retranslateUi(StationQueryDialog)
        QtCore.QMetaObject.connectSlotsByName(StationQueryDialog)

    def retranslateUi(self, StationQueryDialog):
        StationQueryDialog.setWindowTitle(_translate("StationQueryDialog", "Dialog", None))
        self.SNCLGroupBox.setTitle(_translate("StationQueryDialog", "SNCL", None))
        self.locationLabel.setText(_translate("StationQueryDialog", "Locations", None))
        self.networkLabel.setText(_translate("StationQueryDialog", "Networks", None))
        self.channelLabel.setText(_translate("StationQueryDialog", "Channels", None))
        self.stationLabel.setText(_translate("StationQueryDialog", "Stations", None))
        self.stationLineEdit.setText(_translate("StationQueryDialog", "*", None))
        self.networkLineEdit.setText(_translate("StationQueryDialog", "_GSN", None))
        self.locationLineEdit.setText(_translate("StationQueryDialog", "*", None))
        self.channelLineEdit.setText(_translate("StationQueryDialog", "?HZ", None))
        self.timeGroupBox.setTitle(_translate("StationQueryDialog", "Time", None))
        self.timeBetweenRadioButton.setText(_translate("StationQueryDialog", "Between start and end times", None))
        self.starttimeLabel.setText(_translate("StationQueryDialog", "start", None))
        self.endtimeLabele.setText(_translate("StationQueryDialog", "end", None))
        self.timeDuringEventsRadioButton.setText(_translate("StationQueryDialog", "Operational during selected events", None))
        self.locationGroupBox.setTitle(_translate("StationQueryDialog", "Location", None))
        self.locationRangeRadioButton.setText(_translate("StationQueryDialog", "Within lat/lon box", None))
        self.locationDistanceFromPointRadioButton.setText(_translate("StationQueryDialog", "Distance from point", None))
        self.label_8.setText(_translate("StationQueryDialog", "E", None))
        self.label_9.setText(_translate("StationQueryDialog", "N", None))
        self.label_10.setText(_translate("StationQueryDialog", "-", None))
        self.label_11.setText(_translate("StationQueryDialog", "degrees", None))
        self.label_6.setText(_translate("StationQueryDialog", "from", None))
        self.locationDistanceFromEventsRadioButton.setText(_translate("StationQueryDialog", "Distance from selected events", None))
        self.label_3.setText(_translate("StationQueryDialog", "-", None))
        self.label_5.setText(_translate("StationQueryDialog", "degrees", None))

