# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 601)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.result_button = QPushButton(self.centralwidget)
        self.result_button.setObjectName(u"result_button")
        self.result_button.setGeometry(QRect(340, 410, 101, 24))
        self.result_button.setMinimumSize(QSize(101, 0))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(3, 10, 712, 209))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.T_average_air = QLineEdit(self.widget)
        self.T_average_air.setObjectName(u"T_average_air")
        self.T_average_air.setReadOnly(False)
        self.T_average_air.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.T_average_air, 7, 0, 1, 1)

        self.n = QLineEdit(self.widget)
        self.n.setObjectName(u"n")
        self.n.setCursorPosition(11)
        self.n.setReadOnly(False)
        self.n.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.n, 5, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.C_water = QLineEdit(self.widget)
        self.C_water.setObjectName(u"C_water")
        self.C_water.setReadOnly(False)
        self.C_water.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.C_water, 2, 0, 1, 1)

        self.Ro_water = QLineEdit(self.widget)
        self.Ro_water.setObjectName(u"Ro_water")
        self.Ro_water.setReadOnly(False)
        self.Ro_water.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.Ro_water, 3, 0, 1, 1)

        self.T_air = QLineEdit(self.widget)
        self.T_air.setObjectName(u"T_air")
        self.T_air.setReadOnly(False)
        self.T_air.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.T_air, 6, 0, 1, 1)

        self.H_water = QLineEdit(self.widget)
        self.H_water.setObjectName(u"H_water")
        self.H_water.setReadOnly(False)
        self.H_water.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.H_water, 4, 0, 1, 1)

        self.Q_engine_to_radiator = QLineEdit(self.widget)
        self.Q_engine_to_radiator.setObjectName(u"Q_engine_to_radiator")
        self.Q_engine_to_radiator.setEnabled(True)
        self.Q_engine_to_radiator.setDragEnabled(False)
        self.Q_engine_to_radiator.setReadOnly(False)
        self.Q_engine_to_radiator.setPlaceholderText(u"")

        self.gridLayout_2.addWidget(self.Q_engine_to_radiator, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.Q_engine_to_radiator_info = QLabel(self.widget)
        self.Q_engine_to_radiator_info.setObjectName(u"Q_engine_to_radiator_info")

        self.gridLayout_3.addWidget(self.Q_engine_to_radiator_info, 1, 0, 1, 1)

        self.C_water_info = QLabel(self.widget)
        self.C_water_info.setObjectName(u"C_water_info")

        self.gridLayout_3.addWidget(self.C_water_info, 2, 0, 1, 1)

        self.Ro_water_info = QLabel(self.widget)
        self.Ro_water_info.setObjectName(u"Ro_water_info")

        self.gridLayout_3.addWidget(self.Ro_water_info, 3, 0, 1, 1)

        self.H_water_info = QLabel(self.widget)
        self.H_water_info.setObjectName(u"H_water_info")

        self.gridLayout_3.addWidget(self.H_water_info, 4, 0, 1, 1)

        self.n_info = QLabel(self.widget)
        self.n_info.setObjectName(u"n_info")

        self.gridLayout_3.addWidget(self.n_info, 5, 0, 1, 1)

        self.T_air_info = QLabel(self.widget)
        self.T_air_info.setObjectName(u"T_air_info")

        self.gridLayout_3.addWidget(self.T_air_info, 6, 0, 1, 1)

        self.T_average_air_info = QLabel(self.widget)
        self.T_average_air_info.setObjectName(u"T_average_air_info")

        self.gridLayout_3.addWidget(self.T_average_air_info, 7, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 270, 443, 64))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.N_result = QLabel(self.widget1)
        self.N_result.setObjectName(u"N_result")

        self.verticalLayout.addWidget(self.N_result)

        self.F_result = QLabel(self.widget1)
        self.F_result.setObjectName(u"F_result")

        self.verticalLayout.addWidget(self.F_result)

        self.N_fan_result = QLabel(self.widget1)
        self.N_fan_result.setObjectName(u"N_fan_result")

        self.verticalLayout.addWidget(self.N_fan_result)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.N_result_info = QLabel(self.widget1)
        self.N_result_info.setObjectName(u"N_result_info")

        self.verticalLayout_2.addWidget(self.N_result_info)

        self.F_result_info = QLabel(self.widget1)
        self.F_result_info.setObjectName(u"F_result_info")

        self.verticalLayout_2.addWidget(self.F_result_info)

        self.N_fan_result_info = QLabel(self.widget1)
        self.N_fan_result_info.setObjectName(u"N_fan_result_info")

        self.verticalLayout_2.addWidget(self.N_fan_result_info)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.Q_engine_to_radiator, self.C_water)
        QWidget.setTabOrder(self.C_water, self.Ro_water)
        QWidget.setTabOrder(self.Ro_water, self.H_water)
        QWidget.setTabOrder(self.H_water, self.n)
        QWidget.setTabOrder(self.n, self.T_air)
        QWidget.setTabOrder(self.T_air, self.T_average_air)
        QWidget.setTabOrder(self.T_average_air, self.result_button)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.result_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.T_average_air.setText(QCoreApplication.translate("MainWindow", u"T\u0441\u0440.\u0432\u043e\u0437\u0434(K)", None))
        self.n.setText(QCoreApplication.translate("MainWindow", u"n\u0432\u0438(\u043e\u0431/\u043c\u0438\u043d)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.C_water.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0436(\u0414\u0436/\u043a\u0433*\u041a)", None))
        self.Ro_water.setText(QCoreApplication.translate("MainWindow", u"\u03c1(\u043a\u0433/\u043c^3)", None))
        self.T_air.setText(QCoreApplication.translate("MainWindow", u"\u0394T(\u041a)", None))
        self.H_water.setText(QCoreApplication.translate("MainWindow", u"P\u0436(\u041f\u0430)", None))
        self.Q_engine_to_radiator.setText(QCoreApplication.translate("MainWindow", u"Q\u0432(\u0414\u0436/\u0441)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.Q_engine_to_radiator_info.setText(QCoreApplication.translate("MainWindow", u"Q\u0432(\u0414\u0436/\u0441) - \u043a\u043e\u043b-\u0432\u043e \u0442\u0435\u043f\u043b\u0430, \u043e\u0442\u0432\u043e\u0434\u0438\u043c\u043e\u0433\u043e \u043e\u0442 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f \u0438 \u043f\u0435\u0440\u0435\u0434\u0430\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u043e\u0442 \u0432\u043e\u0434\u044b \u043a \u043e\u0445\u043b\u0430\u0436\u0434\u0430\u044e\u0449\u0435\u043c\u0443 \u0432\u043e\u0437\u0434\u0443\u0445\u0443", None))
        self.C_water_info.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0436(\u0414\u0436/\u043a\u0433*\u041a) - \u0441\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u0435\u043f\u043b\u043e\u0435\u043c\u043a\u043e\u0441\u0442\u044c \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438", None))
        self.Ro_water_info.setText(QCoreApplication.translate("MainWindow", u"\u03c1(\u043a\u0433/\u043c^3) - \u0441\u0440\u0435\u0434\u043d\u044f\u044f \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0432\u043e\u0434\u044b", None))
        self.H_water_info.setText(QCoreApplication.translate("MainWindow", u"P\u0436(\u041f\u0430) - \u043d\u0430\u043f\u043e\u0440, \u0441\u043e\u0437\u0434\u0430\u0432\u0430\u0435\u043c\u044b\u0439 \u043d\u0430\u0441\u043e\u0441\u043e\u043c", None))
        self.n_info.setText(QCoreApplication.translate("MainWindow", u"n\u0432\u0438(\u043e\u0431/\u043c\u0438\u043d) - \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f \u043d\u0430\u0441\u043e\u0441\u0430", None))
        self.T_air_info.setText(QCoreApplication.translate("MainWindow", u"\u0394T(\u041a) - \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u043f\u0430\u0434 \u0432\u043e\u0437\u0434\u0443\u0445\u0430 \u0432 \u0440\u0435\u0448\u0435\u0442\u043a\u0435 \u0440\u0430\u0434\u0438\u0430\u0442\u043e\u0440\u0430", None))
        self.T_average_air_info.setText(QCoreApplication.translate("MainWindow", u"T\u0441\u0440.\u0432\u043e\u0437\u0434(K) - \u0441\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043e\u0445\u043b\u0430\u0436\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0432\u043e\u0437\u0434\u0443\u0445\u0430, \u043f\u0440\u043e\u0445\u043e\u0434\u044f\u0449\u0435\u0433\u043e \u0447\u0435\u0440\u0435\u0437 \u0440\u0430\u0434\u0438\u0430\u0442\u043e\u0440", None))
        self.N_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.F_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.N_fan_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.N_result_info.setText(QCoreApplication.translate("MainWindow", u"N\u0432.\u043d(\u041a\u0412\u0442) - \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c, \u043f\u043e\u0442\u0440\u0435\u0431\u043b\u044f\u0435\u043c\u0430\u044f \u0432\u043e\u0434\u044f\u043d\u044b\u043c \u043d\u0430\u0441\u043e\u0441\u043e\u043c", None))
        self.F_result_info.setText(QCoreApplication.translate("MainWindow", u"F(\u043c^2) - \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u0438 \u043e\u0445\u043b\u0430\u0436\u0434\u0435\u043d\u0438\u044f \u0432\u043e\u0434\u044f\u043d\u043e\u0433\u043e \u0440\u0430\u0434\u0438\u0430\u0442\u043e\u0440\u0430", None))
        self.N_fan_result_info.setText(QCoreApplication.translate("MainWindow", u"N\u0432(\u043a\u0412\u0442) - \u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c, \u0437\u0430\u0442\u0440\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u0430\u044f \u043d\u0430 \u043f\u0440\u0438\u0432\u043e\u0434 \u043e\u0441\u0435\u0432\u043e\u0433\u043e \u0432\u0435\u043d\u0442\u0438\u043b\u044f\u0442\u043e\u0440\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u043e\u0445\u0434\u0430\u0436\u0434\u0435\u043d\u0438\u044f", None))
    # retranslateUi

