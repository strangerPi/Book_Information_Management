# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_search_page(object):
    def setupUi(self, search_page):
        search_page.setObjectName("search_page")
        search_page.resize(846, 799)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/查询.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        search_page.setWindowIcon(icon)
        search_page.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(search_page)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(180, 120, 341, 401))
        self.frame_7.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"border-radius:10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(10, 10, 321, 381))
        self.frame_8.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius:5px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.id_search_input = QtWidgets.QLineEdit(self.frame_8)
        self.id_search_input.setGeometry(QtCore.QRect(50, 50, 221, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.id_search_input.setFont(font)
        self.id_search_input.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-radius:0px;\n"
"")
        self.id_search_input.setPlaceholderText("")
        self.id_search_input.setObjectName("id_search_input")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.info_show = QtWidgets.QTextEdit(self.frame_8)
        self.info_show.setGeometry(QtCore.QRect(50, 110, 221, 251))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.info_show.setFont(font)
        self.info_show.setAcceptDrops(True)
        self.info_show.setStyleSheet("border:2px solid grey；")
        self.info_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_show.setFrameShadow(QtWidgets.QFrame.Plain)
        self.info_show.setMidLineWidth(0)
        self.info_show.setReadOnly(True)
        self.info_show.setObjectName("info_show")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 21, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setGeometry(QtCore.QRect(270, 50, 21, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_4.setGeometry(QtCore.QRect(280, 0, 41, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.close_button_s = QtWidgets.QPushButton(self.frame_4)
        self.close_button_s.setGeometry(QtCore.QRect(10, 5, 26, 26))
        self.close_button_s.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(235, 113, 113);\n"
"    text-align:center;\n"
"    border:0px outset rgb(255, 255, 255);\n"
"    border-radius:13px;\n"
"}\n"
"QPushButton:hover {\n"
"    border:-4px outset rgba(36, 36, 36,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    border:4px outset rgba(36, 36, 36,0);\n"
"}\n"
"")
        self.close_button_s.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/关闭白.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button_s.setIcon(icon1)
        self.close_button_s.setObjectName("close_button_s")
        search_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(search_page)
        QtCore.QMetaObject.connectSlotsByName(search_page)

    def retranslateUi(self, search_page):
        _translate = QtCore.QCoreApplication.translate
        search_page.setWindowTitle(_translate("search_page", "MainWindow"))
        self.label_4.setText(_translate("search_page", "输入要查询的书籍名称"))
        self.info_show.setPlaceholderText(_translate("search_page", "   查询结果:库中无此书"))
        self.label_5.setText(_translate("search_page", "《"))
        self.label_6.setText(_translate("search_page", "》"))
import res_rc
