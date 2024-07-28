# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonOpen = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonOpen.sizePolicy().hasHeightForWidth())
        self.ButtonOpen.setSizePolicy(sizePolicy)
        self.ButtonOpen.setMinimumSize(QtCore.QSize(54, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonOpen.setFont(font)
        self.ButtonOpen.setStyleSheet("\n"
"selection-background-color: rgb(255, 68, 21);\n"
"border-color: rgb(255, 97, 100);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../youtube AI creative/indexezd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonOpen.setIcon(icon)
        self.ButtonOpen.setIconSize(QtCore.QSize(50, 14))
        self.ButtonOpen.setCheckable(False)
        self.ButtonOpen.setAutoRepeat(False)
        self.ButtonOpen.setDefault(True)
        self.ButtonOpen.setFlat(True)
        self.ButtonOpen.setObjectName("ButtonOpen")
        self.gridLayout.addWidget(self.ButtonOpen, 0, 0, 2, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 5, 1, 1)
        self.BtnDescribe = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.BtnDescribe.setFont(font)
        self.BtnDescribe.setObjectName("BtnDescribe")
        self.gridLayout_2.addWidget(self.BtnDescribe, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_3.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_3.addWidget(self.comboBox_2, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 4, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonOpen.setText(_translate("Form", "Open CSV"))
        self.BtnDescribe.setText(_translate("Form", "Describe"))
        self.label.setText(_translate("Form", "Columns"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Describe data"))
        self.pushButton.setText(_translate("Form", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Plot Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
