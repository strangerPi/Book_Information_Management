# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_insert_page(object):
    def setupUi(self, insert_page):
        insert_page.setObjectName("insert_page")
        insert_page.resize(771, 715)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/添加.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        insert_page.setWindowIcon(icon)
        insert_page.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(insert_page)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(230, 78, 341, 331))
        self.frame_7.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 127);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 311))
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius:5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 66, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.inserted_button = QtWidgets.QPushButton(self.frame)
        self.inserted_button.setGeometry(QtCore.QRect(110, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.inserted_button.setFont(font)
        self.inserted_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border:2px solid;\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 255, 255);\n"
"    border:2px solid;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(100, 255, 255);\n"
"    border:2px solid;\n"
"    border:4px outset;\n"
"}")
        self.inserted_button.setObjectName("inserted_button")
        self.price_input = QtWidgets.QLineEdit(self.frame)
        self.price_input.setGeometry(QtCore.QRect(80, 200, 220, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.price_input.setFont(font)
        self.price_input.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-radius:0px;")
        self.price_input.setObjectName("price_input")
        self.name_input = QtWidgets.QLineEdit(self.frame)
        self.name_input.setGeometry(QtCore.QRect(80, 100, 220, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.name_input.setFont(font)
        self.name_input.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-radius:0px;")
        self.name_input.setObjectName("name_input")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.writer_input = QtWidgets.QLineEdit(self.frame)
        self.writer_input.setGeometry(QtCore.QRect(80, 150, 220, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.writer_input.setFont(font)
        self.writer_input.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-radius:0px;")
        self.writer_input.setObjectName("writer_input")
        self.id_input = QtWidgets.QLineEdit(self.frame)
        self.id_input.setGeometry(QtCore.QRect(80, 50, 220, 40))
        font = QtGui.QFont()
        font.setFamily("方正准圆_GBK")
        font.setPointSize(14)
        self.id_input.setFont(font)
        self.id_input.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"border-radius:0px;")
        self.id_input.setObjectName("id_input")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(280, 0, 41, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.close_button_i = QtWidgets.QPushButton(self.frame_4)
        self.close_button_i.setGeometry(QtCore.QRect(10, 5, 26, 26))
        self.close_button_i.setStyleSheet("QPushButton{\n"
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
        self.close_button_i.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/关闭白.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button_i.setIcon(icon1)
        self.close_button_i.setObjectName("close_button_i")
        insert_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(insert_page)
        QtCore.QMetaObject.connectSlotsByName(insert_page)
        insert_page.setTabOrder(self.id_input, self.name_input)
        insert_page.setTabOrder(self.name_input, self.writer_input)
        insert_page.setTabOrder(self.writer_input, self.price_input)
        insert_page.setTabOrder(self.price_input, self.inserted_button)
        insert_page.setTabOrder(self.inserted_button, self.close_button_i)

    def retranslateUi(self, insert_page):
        _translate = QtCore.QCoreApplication.translate
        insert_page.setWindowTitle(_translate("insert_page", "MainWindow"))
        self.label_3.setText(_translate("insert_page", "书籍编号"))
        self.label_4.setText(_translate("insert_page", "书籍名称"))
        self.label_5.setText(_translate("insert_page", "书籍作者"))
        self.label_6.setText(_translate("insert_page", "书籍价格"))
        self.inserted_button.setText(_translate("insert_page", "插入数据"))
        self.label.setText(_translate("insert_page", "输入要插入的数据"))
import res_rc
