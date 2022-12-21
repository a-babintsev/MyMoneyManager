# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Forms\UI\expenses_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/dollar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-6, -5, 811, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Images/money_background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ControllMoneyTab = QtWidgets.QTabWidget(self.frame)
        self.ControllMoneyTab.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.ControllMoneyTab.setStyleSheet("QTabBar::tab {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"    background-color: rgb(120, 170, 140);\n"
"}")
        self.ControllMoneyTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.ControllMoneyTab.setObjectName("ControllMoneyTab")
        self.expensesTab = QtWidgets.QWidget()
        self.expensesTab.setObjectName("expensesTab")
        self.label_2 = QtWidgets.QLabel(self.expensesTab)
        self.label_2.setGeometry(QtCore.QRect(-6, -5, 811, 481))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Images/expenses.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(self.expensesTab)
        self.frame_4.setGeometry(QtCore.QRect(-1, -1, 801, 471))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.expenseNameEdit = QtWidgets.QLineEdit(self.frame_5)
        self.expenseNameEdit.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.expenseNameEdit.setObjectName("expenseNameEdit")
        self.verticalLayout_3.addWidget(self.expenseNameEdit)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.ExpenseSumEdit = QtWidgets.QLineEdit(self.frame_6)
        self.ExpenseSumEdit.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.ExpenseSumEdit.setObjectName("ExpenseSumEdit")
        self.verticalLayout_4.addWidget(self.ExpenseSumEdit)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.expenseDateEdit = QtWidgets.QDateEdit(self.frame_7)
        self.expenseDateEdit.setStyleSheet("QDateEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QDateEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.expenseDateEdit.setObjectName("expenseDateEdit")
        self.verticalLayout_5.addWidget(self.expenseDateEdit)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.expenseCategoryComboBox = QtWidgets.QComboBox(self.frame_8)
        self.expenseCategoryComboBox.setStyleSheet("QComboBox {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.expenseCategoryComboBox.setObjectName("expenseCategoryComboBox")
        self.verticalLayout_6.addWidget(self.expenseCategoryComboBox)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.ControllMoneyTab.addTab(self.expensesTab, "")
        self.profitTab = QtWidgets.QWidget()
        self.profitTab.setObjectName("profitTab")
        self.label_3 = QtWidgets.QLabel(self.profitTab)
        self.label_3.setGeometry(QtCore.QRect(-6, -5, 811, 481))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Images/profits.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.frame_9 = QtWidgets.QFrame(self.profitTab)
        self.frame_9.setGeometry(QtCore.QRect(-1, -1, 801, 471))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        self.label_8.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.profitNameEdit = QtWidgets.QLineEdit(self.frame_10)
        self.profitNameEdit.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.profitNameEdit.setObjectName("profitNameEdit")
        self.verticalLayout_10.addWidget(self.profitNameEdit)
        self.verticalLayout_11.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_11)
        self.label_9.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.profitSumEdit = QtWidgets.QLineEdit(self.frame_11)
        self.profitSumEdit.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.profitSumEdit.setObjectName("profitSumEdit")
        self.verticalLayout_9.addWidget(self.profitSumEdit)
        self.verticalLayout_11.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_12)
        self.label_10.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.profitDateEdit = QtWidgets.QDateEdit(self.frame_12)
        self.profitDateEdit.setStyleSheet("QDateEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QDateEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.profitDateEdit.setObjectName("profitDateEdit")
        self.verticalLayout_8.addWidget(self.profitDateEdit)
        self.verticalLayout_11.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        self.label_11.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.profitCategoryEdit = QtWidgets.QComboBox(self.frame_13)
        self.profitCategoryEdit.setStyleSheet("QComboBox {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.profitCategoryEdit.setObjectName("profitCategoryEdit")
        self.verticalLayout_7.addWidget(self.profitCategoryEdit)
        self.verticalLayout_11.addWidget(self.frame_13)
        self.ControllMoneyTab.addTab(self.profitTab, "")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, 499, 801, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.infoLbl = QtWidgets.QLabel(self.frame_3)
        self.infoLbl.setEnabled(True)
        self.infoLbl.setStyleSheet("color: white;\n"
"background-color: rgb(44, 153, 255);\n"
"font: 15px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"font-weight: bold;")
        self.infoLbl.setObjectName("infoLbl")
        self.horizontalLayout_2.addWidget(self.infoLbl)
        self.backMenuBtn = QtWidgets.QPushButton(self.frame_3)
        self.backMenuBtn.setStyleSheet("QPushButton#backMenuBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#backMenuBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.backMenuBtn.setObjectName("backMenuBtn")
        self.horizontalLayout_2.addWidget(self.backMenuBtn)
        self.clearFormBtn = QtWidgets.QPushButton(self.frame_3)
        self.clearFormBtn.setStyleSheet("QPushButton#clearFormBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#clearFormBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.clearFormBtn.setObjectName("clearFormBtn")
        self.horizontalLayout_2.addWidget(self.clearFormBtn)
        self.addBtn = QtWidgets.QPushButton(self.frame_3)
        self.addBtn.setStyleSheet("QPushButton#addBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#addBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_2.addWidget(self.addBtn)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ControllMoneyTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyMoneyManager"))
        self.label_4.setText(_translate("MainWindow", "Название"))
        self.label_5.setText(_translate("MainWindow", "Сумма"))
        self.label_6.setText(_translate("MainWindow", "Дата покупки"))
        self.label_7.setText(_translate("MainWindow", "Категория"))
        self.ControllMoneyTab.setTabText(self.ControllMoneyTab.indexOf(self.expensesTab), _translate("MainWindow", "Добавить расход"))
        self.label_8.setText(_translate("MainWindow", "Название"))
        self.label_9.setText(_translate("MainWindow", "Сумма"))
        self.label_10.setText(_translate("MainWindow", "Дата заработка"))
        self.label_11.setText(_translate("MainWindow", "Категория"))
        self.ControllMoneyTab.setTabText(self.ControllMoneyTab.indexOf(self.profitTab), _translate("MainWindow", "Добавить доход"))
        self.infoLbl.setText(_translate("MainWindow", "Запись успешно добавлена!"))
        self.backMenuBtn.setText(_translate("MainWindow", "Назад"))
        self.clearFormBtn.setText(_translate("MainWindow", "Очистить"))
        self.addBtn.setText(_translate("MainWindow", "Добавить"))
from Pictures.Images import add_expenses_form


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())