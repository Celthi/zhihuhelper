# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created: Sat Sep 05 17:46:33 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 521, 421))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.defaultAccount = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.defaultAccount.setObjectName(_fromUtf8("defaultAccount"))
        self.verticalLayout.addWidget(self.defaultAccount)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.myAccount = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.myAccount.setObjectName(_fromUtf8("myAccount"))
        self.verticalLayout_3.addWidget(self.myAccount)
        self.account = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.account.setObjectName(_fromUtf8("account"))
        self.verticalLayout_3.addWidget(self.account)
        self.password = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName(_fromUtf8("password"))
        self.verticalLayout_3.addWidget(self.password)
        self.verifycode_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.verifycode_label.setObjectName(_fromUtf8("verifycode_label"))
        self.verticalLayout_3.addWidget(self.verifycode_label)
        self.GetVerifycode = QtGui.QPushButton(self.verticalLayoutWidget)
        self.GetVerifycode.setObjectName(_fromUtf8("GetVerifycode"))
        self.verticalLayout_3.addWidget(self.GetVerifycode)
        self.verifycode = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.verifycode.setObjectName(_fromUtf8("verifycode"))
        self.verticalLayout_3.addWidget(self.verifycode)
        self.answers = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.answers.setObjectName(_fromUtf8("answers"))
        self.verticalLayout_3.addWidget(self.answers)
        self.PicQuality = QtGui.QComboBox(self.verticalLayoutWidget)
        self.PicQuality.setObjectName(_fromUtf8("PicQuality"))
        self.PicQuality.addItem(_fromUtf8(""))
        self.PicQuality.addItem(_fromUtf8(""))
        self.PicQuality.addItem(_fromUtf8(""))
        self.PicQuality.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.PicQuality)
        self.thread_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.thread_label.setObjectName(_fromUtf8("thread_label"))
        self.verticalLayout_3.addWidget(self.thread_label)
        self.threads = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.threads.setObjectName(_fromUtf8("threads"))
        self.verticalLayout_3.addWidget(self.threads)
        self.Login = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Login.setObjectName(_fromUtf8("Login"))
        self.verticalLayout_3.addWidget(self.Login)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ZhihuHelper", None))
        self.defaultAccount.setText(_translate("MainWindow", "Logging with default account", None))
        self.myAccount.setText(_translate("MainWindow", "Logging with the following Account", None))
        self.verifycode_label.setText(_translate("MainWindow", "TextLabel", None))
        self.GetVerifycode.setText(_translate("MainWindow", "GetVerifyCode", None))
        self.PicQuality.setItemText(0, _translate("MainWindow", "图片质量", None))
        self.PicQuality.setItemText(1, _translate("MainWindow", "高清", None))
        self.PicQuality.setItemText(2, _translate("MainWindow", "标准", None))
        self.PicQuality.setItemText(3, _translate("MainWindow", "无图", None))
        self.thread_label.setText(_translate("MainWindow", "线程数", None))
        self.Login.setText(_translate("MainWindow", "Login", None))

