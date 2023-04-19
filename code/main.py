import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from login import *
from mainpage import *
from search import *
from insert import *
from delete import *
from update import *

global ordertype

#  创建数字限定校验器，让某些输入框只能输入10位数字，例如书籍编号输入框
num = QRegExpValidator(QRegExp("^[0-9]\\d{9}$"))


class loginppage(QMainWindow, Ui_login_page):  # 登录界面的类
    __start_pos = None
    __end_pos = None
    __is_tracking = False

    def __init__(self):  # 登录界面初始化以及信号与槽函数的连接
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口无边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.login_button.clicked.connect(self.sign)
        self.quit_button.clicked.connect(self.closewin)
        self.main = mainpage()  # 主界面类实例化
        self.logininit()

        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 创建窗口边框阴影
        self.add_shadow()

    def add_shadow(self):  # 设置边框阴影的值
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(3)
        self.effect_shadow.setColor(QtCore.Qt.gray)
        self.frame.setGraphicsEffect(self.effect_shadow)
        self.frame_2.setGraphicsEffect(self.effect_shadow)
        self.quit_button.setGraphicsEffect(self.effect_shadow)
        self.login_button.setGraphicsEffect(self.effect_shadow)

    def logininit(self):  # 默认状态下输入正确账号密码
        self.user_input.setText('admin')
        self.pwd_input.setText('admin')

    def create_mainpage(self):  # 创建主界面
        self.main.show()

    def closewin(self):  # 关闭页面
        self.close()

    def sign(self):  # 关闭页面
        a = self.user_input.text()
        b = self.pwd_input.text()
        if a == "admin" and b == "admin":  # 如账号密码正确就关闭登录窗口以及创建主页面
            self.close()
            self.create_mainpage()
        else:
            message = QMessageBox()
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('登录失败')
            message.setText("账号或密码错误    ")
            message.exec_()

    # 通过三个QMouseEvent事件来实现无边框下的窗口拖动
    def mouseMoveEvent(self, event_: QMouseEvent):
        if self.__is_tracking:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


class mainpage(QMainWindow, Ui_book_mainpage):  # 主页面的类
    __start_pos = None
    __end_pos = None
    __is_tracking = False

    def __init__(self):  # 主界面初始化
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pageinit()
        self.show_data()
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 创建窗口边框阴影
        self.add_shadow()
        self.delete = deletepage()
        self.search = searchpage()
        self.insert = insertpage()
        self.update = updatepage()

    def add_shadow(self):  # 设置边框阴影的值
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(3)
        self.effect_shadow.setColor(QtCore.Qt.gray)
        self.centralwidget.setGraphicsEffect(self.effect_shadow)
        self.mini_button.setGraphicsEffect(self.effect_shadow)
        self.close_button.setGraphicsEffect(self.effect_shadow)

    def pageinit(self):  # 主界面按钮信号与槽函数的连接
        global ordertype
        ordertype = 'asc'

        self.show_button.clicked.connect(self.show_data)
        self.search_button.clicked.connect(self.searchpage)
        self.search_button.clicked.connect(self.search_open)
        self.insert_button.clicked.connect(self.insertpage)
        self.insert_button.clicked.connect(self.insert_open)
        self.delete_button.clicked.connect(self.deletepage)
        self.delete_button.clicked.connect(self.delete_open)
        self.update_button.clicked.connect(self.updatepage)
        self.update_button.clicked.connect(self.update_open)
        self.sort_button.clicked.connect(self.show_data_order)
        self.deduplicate_button.clicked.connect(self.deduplicate)
        self.close_button.clicked.connect(self.closeall)
        self.mini_button.clicked.connect(self.mini)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置tableWidget水平界面自适应
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置tableWidget水平界面自适应

    @staticmethod
    def closeall():  # 主页面关闭连带整个应用退出
        QApplication.instance().quit()

    def mini(self):  # 主页面最小化
        self.showMinimized()

    def show_data(self):  # 将sqlite3库中数据显示到tableWidget
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM book order by id"  # noqa
        cursor.execute(sql)
        data = cursor.fetchall()
        rows = str(len(data))
        self.tableWidget.setRowCount(len(data))
        # 遍历每一行每一列将数据显示到tableWidget
        x = 0
        for _ in data:
            y = 0
            for _ in _:
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                self.tableWidget.item(x, y).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置tableWidget数据居中
                y = y + 1
            x = x + 1
        # 创建一个列表接收数据库book表中price列的数据，max( )获得库中书籍最高价格
        datalist = []
        for price in data:
            datalist.append(price[3])
        if datalist:
            sql = "select * from book where price  like '%%%%%d%%%%'" % (int(max(datalist)))  # noqa
            cursor.execute(sql)
            data = cursor.fetchone()
            self.book_quantity.setText(
                '库中共有' + rows + '本书籍,最贵的书籍是《' + data[1] + '》,该书价格为' + str(max(datalist)) + '元')
        else:
            self.book_quantity.setText('库中暂无书籍')
        cursor.close()
        conn.close()

    def show_data_order(self):  # 按价格排序函数
        global ordertype
        if ordertype == 'desc':  # 每次点击排序按钮反转排序方式（升序、降序）
            ordertype = 'asc'
        else:
            ordertype = 'desc'
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        sql = "SELECT * FROM book order by price %s" % ordertype  # noqa
        cursor.execute(sql)
        data = cursor.fetchall()
        self.tableWidget.setRowCount(len(data))
        x = 0
        for _ in data:
            y = 0
            for _ in _:
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                self.tableWidget.item(x, y).setTextAlignment(0x0004 | 0x0080)
                # self.tableWidget.item(x, y).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                y = y + 1
            x = x + 1
        cursor.close()
        conn.close()

    def deduplicate(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("delete from book where name in (select name from book "  # noqa
                       "group by   name   having count(name) > 1)  "  # noqa
                       "and rowid not in (select min(rowid) from   "  # noqa
                       "book group by name having count(name  )>1) ")  # noqa
        conn.commit()
        cursor.close()
        conn.close()
        message = QMessageBox()
        message.setFont(QFont("微软雅黑", 14))
        message.setWindowTitle("success")
        message.setText("        去重成功!\n\n书籍库中重复书籍只  \n保留最先添加的一本  ")
        message.exec_()
        self.show_data()

    # 从上之下分别是更新、删除、查询、插入的类实例化
    def updatepage(self):
        self.update = updatepage()
        self.update.show()
        # self.update.move(1265, 70)
        self.update.signal.connect(self.show_data)

    def deletepage(self):
        self.delete = deletepage()
        self.delete.show()
        # self.delete.move(1265, 70)
        self.delete.signal.connect(self.show_data)

    def searchpage(self):
        self.search = searchpage()
        self.search.show()
        # self.search.move(1265, 70)

    def insertpage(self):
        self.insert = insertpage()
        self.insert.show()
        # self.insert.move(1265, 70)
        self.insert.signal.connect(self.show_data)

    def insert_open(self):  # 某界面打开时隐藏其他所有界面
        self.update.hide()
        self.delete.hide()
        self.search.hide()

    def search_open(self):
        self.insert.hide()
        self.delete.hide()
        self.update.hide()

    def delete_open(self):
        self.insert.hide()
        self.update.hide()
        self.search.hide()

    def update_open(self):
        self.insert.hide()
        self.delete.hide()
        self.search.hide()

    # 通过三个QMouseEvent事件来实现无边框下的窗口拖动
    def mouseMoveEvent(self, event_: QMouseEvent):
        if self.__is_tracking:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


class searchpage(QMainWindow, Ui_search_page):  # 搜索界面的类
    __start_pos = None
    __end_pos = None
    __is_tracking = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button_s.clicked.connect(self.ani_close)
        self.id_search_input.textChanged.connect(self.search_data)
        self.animation = QPropertyAnimation(self.frame_7, b'size')  #
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 创建窗口边框阴影
        self.add_shadow()
        self.ani_open()

    def ani_close(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(341, 401))
        self.animation.setEndValue(QSize(0, 0))
        self.animation.start()
        self.animation.finished.connect(self.close)

    def ani_open(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(0, 0))
        self.animation.setEndValue(QSize(341, 401))
        self.animation.start()

    def add_shadow(self):  # 设置边框阴影的值
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(4)
        self.effect_shadow.setColor(QtCore.Qt.gray)
        self.centralwidget.setGraphicsEffect(self.effect_shadow)
        self.close_button_s.setGraphicsEffect(self.effect_shadow)

    def search_data(self):  # 按输入id进行书籍信息的搜索
        if self.id_search_input.text():
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            sql = "select * from book where name  like '%%%%%s%%%%'" % (self.id_search_input.text())  # noqa
            cursor.execute(sql)
            data_searched = cursor.fetchone()
            if data_searched:
                self.info_show.setText('书籍编号:' + str(data_searched[0]) + '\n' * 2 +
                                       '书籍价格:' + str(data_searched[3]) + '\n' * 2 +
                                       '书籍名称:' + '\n《' + str(data_searched[1]) + '》\n' + '\n' +
                                       '书籍作者:' + '\n" ' + str(data_searched[2]) + ' "\n'
                                       )
            cursor.close()
            conn.close()
        else:
            self.info_show.clear()

    def mouseMoveEvent(self, event_: QMouseEvent):
        if self.__is_tracking:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


class insertpage(QMainWindow, Ui_insert_page):  # 插入界面的类
    _signal = pyqtSignal()  # noqa
    __start_pos = None
    __end_pos = None
    __is_tracking = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.inserted_button.clicked.connect(self.insert_data)
        self.inserted_button.clicked.connect(self.givesignal)
        self.id_input.setValidator(num)
        self.price_input.setValidator(num)
        self.close_button_i.clicked.connect(self.ani_close)
        self.animation = QPropertyAnimation(self.frame_7, b'size')
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 创建窗口边框阴影
        self.add_shadow()
        self.ani_open()

    def ani_close(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(341, 331))
        self.animation.setEndValue(QSize(0, 0))
        self.animation.start()
        self.animation.finished.connect(self.close)

    def ani_open(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(0, 0))
        self.animation.setEndValue(QSize(341, 331))
        self.animation.start()

    def add_shadow(self):  # 设置边框阴影的值
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(4)
        self.effect_shadow.setColor(QtCore.Qt.gray)
        self.centralwidget.setGraphicsEffect(self.effect_shadow)
        self.close_button_i.setGraphicsEffect(self.effect_shadow)
        # self.inserted_button.setGraphicsEffect(self.effect_shadow)

    def givesignal(self):  # 传递空信号给mainpage类以便插入信息后更新到表中
        self._signal.emit()

    def insert_data(self):
        # 输入信息完整才能成功插入信息
        message = QMessageBox()
        if self.id_input.text() and self.name_input.text and self.writer_input.text() and self.price_input.text():
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            sql = "insert or ignore into book(id, name, writer, price)values(?,?,?,?)"  # noqa
            id_inserted = int(self.id_input.text())
            name_inserted = self.name_input.text()
            writer_inserted = self.writer_input.text()
            price_inserted = int(self.price_input.text())
            data = (id_inserted, name_inserted, writer_inserted, price_inserted)
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('添加成功')
            message.setText("书籍已添加到库中    ")
            message.exec_()
            self.close()
        else:
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('添加失败')
            message.setText("输入内容有缺失    ")
            message.exec_()

    @property
    def signal(self):
        return self._signal

    def mouseMoveEvent(self, event_: QMouseEvent):
        if self.__is_tracking:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


class deletepage(QMainWindow, Ui_delete_page):  # 删除界面的类
    __start_pos = None
    __end_pos = None
    __is_tracking = False
    _signal = pyqtSignal()  # noqa

    @property
    def signal(self):
        return self._signal

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.deleted_button.clicked.connect(self.delete_data)
        self.deleted_button.clicked.connect(self.givesignal)
        self.id_deleted_input.setValidator(num)
        self.close_button_d.clicked.connect(self.ani_close)
        self.animation = QPropertyAnimation(self.frame_7, b'size')
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 创建窗口边框阴影
        self.add_shadow()
        self.ani_open()

    def ani_close(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(251, 221))
        self.animation.setEndValue(QSize(0, 0))
        self.animation.start()
        self.animation.finished.connect(self.close)

    def ani_open(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(0, 0))
        self.animation.setEndValue(QSize(251, 221))
        self.animation.start()

    def add_shadow(self):  # 设置边框阴影的值
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(4)
        self.effect_shadow.setColor(QtCore.Qt.gray)
        self.centralwidget.setGraphicsEffect(self.effect_shadow)
        self.close_button_d.setGraphicsEffect(self.effect_shadow)
        # self.deleted_button.setGraphicsEffect(self.effect_shadow)

    def givesignal(self):  # 传递更新信号
        self._signal.emit()

    def delete_data(self):
        message = QMessageBox()
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        sql = "select id from book"  # noqa
        cursor.execute(sql)
        data = cursor.fetchall()
        datalist = []
        for _ in data:
            datalist.append(_[0])
        # 输入了待删除书籍编号且该编号存在
        if self.id_deleted_input.text() and int(self.id_deleted_input.text()) in datalist:
            sql = "delete from book where id=%s" % (self.id_deleted_input.text())  # noqa
            cursor.execute(sql)
            conn.commit()
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('删除成功')
            message.setText("书籍已从库中去除    ")
            message.exec_()
            self.close()
        # 输入了待删除书籍编号但编号不存在
        elif self.id_deleted_input.text():
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('输入内容有误')
            message.setText("该书籍编号不存在    ")
            message.exec_()
        # 未输入数据
        else:
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('输入内容有缺失')
            message.setText("请重新输入数据    ")
            message.exec_()

        cursor.close()
        conn.close()

    def mouseMoveEvent(self, event_: QMouseEvent):
        if self.__is_tracking:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


class updatepage(QMainWindow, Ui_update_page):  # 更新界面的类
    __start_pos = None
    __end_pos = None
    __is_tracking = False
    _signal = pyqtSignal()  # noqa

    @property
    def signal(self):
        return self._signal

    def givesignal(self):
        self._signal.emit()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.updated_button.clicked.connect(self.update_data_from_id)
        self.updated_button.clicked.connect(self.givesignal)
        self.data_updated.textChanged.connect(self.id_synchronize)
        self.data_updated.setValidator(num)
        self.id_input.setValidator(num)
        self.price_input.setValidator(num)
        self.close_button_u.clicked.connect(self.ani_close)
        self.animation = QPropertyAnimation(self.frame_7, b'size')
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)  # 创建窗口边框阴影
        self.add_shadow()
        self.ani_open()

    def ani_close(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(381, 461))
        self.animation.setEndValue(QSize(0, 0))
        self.animation.start()
        self.animation.finished.connect(self.close)

    def ani_open(self):
        self.animation.setDuration(100)
        self.animation.setStartValue(QSize(0, 0))
        self.animation.setEndValue(QSize(381, 461))
        self.animation.start()

    def add_shadow(self):  # 设置边框阴影的值
        self.effect_shadow.setOffset(0, 0)
        self.effect_shadow.setBlurRadius(4)
        self.effect_shadow.setColor(QtCore.Qt.gray)
        self.centralwidget.setGraphicsEffect(self.effect_shadow)
        self.close_button_u.setGraphicsEffect(self.effect_shadow)
        # self.updated_button.setGraphicsEffect(self.effect_shadow)

    def id_synchronize(self):  # 动态检索待更新书籍信息
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        if self.data_updated.text():
            sql = "select * from book where id=%s" % (self.data_updated.text())  # noqa
            cursor.execute(sql)
            data_searched = cursor.fetchone()
            if data_searched:
                self.id_input.setText(str(data_searched[0]))
                self.name_input.setText(str(data_searched[1]))
                self.writer_input.setText(str(data_searched[2]))
                self.price_input.setText(str(data_searched[3]))
        else:
            self.id_input.clear()
            self.name_input.clear()
            self.writer_input.clear()
            self.price_input.clear()
        conn.commit()
        cursor.close()
        conn.close()

    def update_data_from_id(self):  # 从id来更新书籍信息
        message = QMessageBox()
        if self.data_updated.text():
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            id_updated_input = int(self.data_updated.text())
            id_input = int(self.id_input.text())
            name_input = self.name_input.text()
            writer_input = self.writer_input.text()
            price_input = int(self.price_input.text())
            # 更新逻辑
            # 第一行命令先更新id，后面三行命令从按已更新的id来更新其他三项信息
            cursor.execute("update book set id ='%d' where id='%d'" % (id_input, id_updated_input))  # noqa
            cursor.execute("update book set name ='%s' where id='%d'" % (name_input, id_input))  # noqa
            cursor.execute("update book set writer ='%s' where id='%d'" % (writer_input, id_input))  # noqa
            cursor.execute("update book set price ='%d' where id='%d'" % (price_input, id_input))  # noqa
            conn.commit()
            cursor.close()
            conn.close()
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('更新成功')
            message.setText("书籍已更新完成    ")
            message.exec_()
            self.close()
        else:
            message.setFont(QFont("微软雅黑", 13))
            message.setWindowTitle('输入内容有缺失')
            message.setText("请重新输入数据    ")
            message.exec_()

    def mouseMoveEvent(self, event_: QMouseEvent):
        if self.__is_tracking:
            self.__end_pos = event_.pos() - self.__start_pos
            self.move(self.pos() + self.__end_pos)

    def mousePressEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = True
            self.__start_pos = QPoint(event_.x(), event_.y())

    def mouseReleaseEvent(self, event_: QMouseEvent):
        if event_.button() == Qt.LeftButton:
            self.__is_tracking = False
            self.__start_pos = None
            self.__end_pos = None


def create_table():  # 如无表则创建以免报错
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    sql = """CREATE TABLE if not exists book(
              id INTEGER PRIMARY KEY,
              name text,
              writer text,
              price INTEGER)"""  # noqa
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # pyinstaller -F -w main.py delete.py login.py mainpage.py update.py insert.py search.py res_rc.py 
    create_table()
    app = QApplication(sys.argv)  # 实例化，传参
    app.setStyle('Fusion')  # fusion风格
    win = loginppage()  # 创建登录界面类实例
    win.show()  # 创建窗口
    sys.exit(app.exec())
