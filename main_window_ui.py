# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(653, 554)
        self.stackMain = QStackedWidget(Dialog)
        self.stackMain.setObjectName(u"stackMain")
        self.stackMain.setEnabled(False)
        self.stackMain.setGeometry(QRect(-1, 9, 593, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackMain.sizePolicy().hasHeightForWidth())
        self.stackMain.setSizePolicy(sizePolicy)
        self.pageLanding = QWidget()
        self.pageLanding.setObjectName(u"pageLanding")
        sizePolicy.setHeightForWidth(self.pageLanding.sizePolicy().hasHeightForWidth())
        self.pageLanding.setSizePolicy(sizePolicy)
        self.btnSignupPage = QPushButton(self.pageLanding)
        self.btnSignupPage.setObjectName(u"btnSignupPage")
        self.btnSignupPage.setEnabled(False)
        self.btnSignupPage.setGeometry(QRect(230, 150, 121, 41))
        self.btnSignupPage.setFlat(False)
        self.btnLoginPage = QPushButton(self.pageLanding)
        self.btnLoginPage.setObjectName(u"btnLoginPage")
        self.btnLoginPage.setEnabled(False)
        self.btnLoginPage.setGeometry(QRect(228, 198, 120, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnLoginPage.sizePolicy().hasHeightForWidth())
        self.btnLoginPage.setSizePolicy(sizePolicy1)
        self.textBrowser = QTextBrowser(self.pageLanding)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(200, 70, 181, 41))
        self.stackMain.addWidget(self.pageLanding)
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        self.btnLogin = QPushButton(self.pageLogin)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(230, 220, 131, 51))
        self.btnBackLogin = QPushButton(self.pageLogin)
        self.btnBackLogin.setObjectName(u"btnBackLogin")
        self.btnBackLogin.setGeometry(QRect(20, 20, 75, 24))
        self.textLoginEmail = QLineEdit(self.pageLogin)
        self.textLoginEmail.setObjectName(u"textLoginEmail")
        self.textLoginEmail.setGeometry(QRect(200, 140, 201, 31))
        self.textLoginPassword = QLineEdit(self.pageLogin)
        self.textLoginPassword.setObjectName(u"textLoginPassword")
        self.textLoginPassword.setGeometry(QRect(200, 180, 201, 31))
        self.textLoginPassword.setEchoMode(QLineEdit.Password)
        self.stackMain.addWidget(self.pageLogin)
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.btnLogout = QPushButton(self.pageDashboard)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setGeometry(QRect(10, 20, 91, 31))
        self.btnAddPasswordPage = QPushButton(self.pageDashboard)
        self.btnAddPasswordPage.setObjectName(u"btnAddPasswordPage")
        self.btnAddPasswordPage.setGeometry(QRect(440, 380, 121, 41))
        self.btnDeleteUser = QPushButton(self.pageDashboard)
        self.btnDeleteUser.setObjectName(u"btnDeleteUser")
        self.btnDeleteUser.setGeometry(QRect(10, 60, 91, 31))
        self.tableEntriesWidget = QTableWidget(self.pageDashboard)
        self.tableEntriesWidget.setObjectName(u"tableEntriesWidget")
        self.tableEntriesWidget.setGeometry(QRect(115, 11, 441, 361))
        self.tableEntriesWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.btnRevealPasswords = QPushButton(self.pageDashboard)
        self.btnRevealPasswords.setObjectName(u"btnRevealPasswords")
        self.btnRevealPasswords.setGeometry(QRect(310, 380, 121, 41))
        self.stackMain.addWidget(self.pageDashboard)
        self.pageSignup = QWidget()
        self.pageSignup.setObjectName(u"pageSignup")
        self.pageSignup.setMaximumSize(QSize(593, 301))
        self.btnSignup = QPushButton(self.pageSignup)
        self.btnSignup.setObjectName(u"btnSignup")
        self.btnSignup.setGeometry(QRect(230, 220, 111, 41))
        self.btnBackSignup = QPushButton(self.pageSignup)
        self.btnBackSignup.setObjectName(u"btnBackSignup")
        self.btnBackSignup.setGeometry(QRect(30, 30, 75, 24))
        self.textSignupEmail = QLineEdit(self.pageSignup)
        self.textSignupEmail.setObjectName(u"textSignupEmail")
        self.textSignupEmail.setGeometry(QRect(190, 140, 201, 31))
        self.textSignupPassword = QLineEdit(self.pageSignup)
        self.textSignupPassword.setObjectName(u"textSignupPassword")
        self.textSignupPassword.setGeometry(QRect(190, 180, 201, 31))
        self.textSignupPassword.setEchoMode(QLineEdit.Password)
        self.stackMain.addWidget(self.pageSignup)
        self.pagePassword = QWidget()
        self.pagePassword.setObjectName(u"pagePassword")
        self.stackMain.addWidget(self.pagePassword)
        self.pageAddPassword = QWidget()
        self.pageAddPassword.setObjectName(u"pageAddPassword")
        self.btnAddPassword = QPushButton(self.pageAddPassword)
        self.btnAddPassword.setObjectName(u"btnAddPassword")
        self.btnAddPassword.setGeometry(QRect(300, 180, 101, 31))
        self.btnCancelAddPassword = QPushButton(self.pageAddPassword)
        self.btnCancelAddPassword.setObjectName(u"btnCancelAddPassword")
        self.btnCancelAddPassword.setGeometry(QRect(160, 180, 101, 31))
        self.textOrganization = QLineEdit(self.pageAddPassword)
        self.textOrganization.setObjectName(u"textOrganization")
        self.textOrganization.setGeometry(QRect(160, 30, 251, 31))
        self.textUsername = QLineEdit(self.pageAddPassword)
        self.textUsername.setObjectName(u"textUsername")
        self.textUsername.setGeometry(QRect(160, 70, 251, 31))
        self.textPassword = QLineEdit(self.pageAddPassword)
        self.textPassword.setObjectName(u"textPassword")
        self.textPassword.setGeometry(QRect(160, 110, 251, 31))
        self.textPassword.setEchoMode(QLineEdit.Password)
        self.stackMain.addWidget(self.pageAddPassword)

        self.retranslateUi(Dialog)

        self.stackMain.setCurrentIndex(2)
        self.btnSignupPage.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btnSignupPage.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.btnLoginPage.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt;\">Password Manager</span></p></body></html>", None))
        self.btnLogin.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.btnBackLogin.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.textLoginEmail.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.textLoginPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.btnLogout.setText(QCoreApplication.translate("Dialog", u"Logout", None))
        self.btnAddPasswordPage.setText(QCoreApplication.translate("Dialog", u"Add Password", None))
        self.btnDeleteUser.setText(QCoreApplication.translate("Dialog", u"Delete User", None))
        self.btnRevealPasswords.setText(QCoreApplication.translate("Dialog", u"Reveal Passwords", None))
        self.btnSignup.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.btnBackSignup.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.textSignupEmail.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email", None))
        self.textSignupPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.btnAddPassword.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.btnCancelAddPassword.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.textOrganization.setPlaceholderText(QCoreApplication.translate("Dialog", u"Organization", None))
        self.textUsername.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.textPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

