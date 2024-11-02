# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugins/lrclib_lyrics/option_lrclib_lyrics.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionLrclibLyrics(object):
    def setupUi(self, OptionLrclibLyrics):
        OptionLrclibLyrics.setObjectName("OptionLrclibLyrics")
        OptionLrclibLyrics.resize(432, 368)
        self.verticalLayout = QtWidgets.QVBoxLayout(OptionLrclibLyrics)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(OptionLrclibLyrics)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lyrics = QtWidgets.QCheckBox(self.groupBox)
        self.lyrics.setObjectName("lyrics")
        self.verticalLayout_2.addWidget(self.lyrics)
        self.syncedlyrics = QtWidgets.QCheckBox(self.groupBox)
        self.syncedlyrics.setEnabled(False)
        self.syncedlyrics.setCheckable(False)
        self.syncedlyrics.setObjectName("syncedlyrics")
        self.verticalLayout_2.addWidget(self.syncedlyrics)
        self.replace_embedded = QtWidgets.QCheckBox(self.groupBox)
        self.replace_embedded.setObjectName("replace_embedded")
        self.verticalLayout_2.addWidget(self.replace_embedded)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(OptionLrclibLyrics)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lrc_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.lrc_name.setObjectName("lrc_name")
        self.verticalLayout_3.addWidget(self.lrc_name)
        self.export_lyrics = QtWidgets.QCheckBox(self.groupBox_2)
        self.export_lyrics.setObjectName("export_lyrics")
        self.verticalLayout_3.addWidget(self.export_lyrics)
        self.replace_exported = QtWidgets.QCheckBox(self.groupBox_2)
        self.replace_exported.setObjectName("replace_exported")
        self.verticalLayout_3.addWidget(self.replace_exported)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(OptionLrclibLyrics)
        QtCore.QMetaObject.connectSlotsByName(OptionLrclibLyrics)

    def retranslateUi(self, OptionLrclibLyrics):
        _translate = QtCore.QCoreApplication.translate
        OptionLrclibLyrics.setWindowTitle(_translate("OptionLrclibLyrics", "Form"))
        self.groupBox.setTitle(_translate("OptionLrclibLyrics", "Embedded Lyrics Options"))
        self.lyrics.setText(_translate("OptionLrclibLyrics", "Download and embed unsynced lyrics"))
        self.syncedlyrics.setText(_translate("OptionLrclibLyrics", "Download and embed synced lyrics"))
        self.replace_embedded.setText(_translate("OptionLrclibLyrics", "Never replace any embedded lyrics if already present"))
        self.groupBox_2.setTitle(_translate("OptionLrclibLyrics", "Lrc Files Options"))
        self.label.setText(_translate("OptionLrclibLyrics", "Use the following name pattern for lrc files:"))
        self.export_lyrics.setText(_translate("OptionLrclibLyrics", "Export lyrics to lrc file when saving (priority to synced lyrics)"))
        self.replace_exported.setText(_translate("OptionLrclibLyrics", "Never replace lrc files if already present"))
