from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dollar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.background_image_menu = QtWidgets.QLabel(self.frame)
        self.background_image_menu.setGeometry(QtCore.QRect(-6, -5, 811, 611))
        self.background_image_menu.setText("")
        self.background_image_menu.setPixmap(QtGui.QPixmap(":/images/money_background.jpg"))
        self.background_image_menu.setScaledContents(True)
        self.background_image_menu.setObjectName("background_image_menu")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.showExpensesFormBtn = QtWidgets.QPushButton(self.frame_4)
        self.showExpensesFormBtn.setStyleSheet("QPushButton#showExpensesFormBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 15px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#showExpensesFormBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.showExpensesFormBtn.setObjectName("showExpensesFormBtn")
        self.verticalLayout_3.addWidget(self.showExpensesFormBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.showStatisticFormBtn = QtWidgets.QPushButton(self.frame_4)
        self.showStatisticFormBtn.setStyleSheet("QPushButton#showStatisticFormBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 15px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#showStatisticFormBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.showStatisticFormBtn.setObjectName("showStatisticFormBtn")
        self.verticalLayout_3.addWidget(self.showStatisticFormBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.showAimsFormBtn = QtWidgets.QPushButton(self.frame_4)
        self.showAimsFormBtn.setStyleSheet("QPushButton#showAimsFormBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 15px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#showAimsFormBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.showAimsFormBtn.setObjectName("showAimsFormBtn")
        self.verticalLayout_3.addWidget(self.showAimsFormBtn)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout.addWidget(self.frame_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????? ???????????? ????????????????"))
        self.showExpensesFormBtn.setText(_translate("MainWindow", "???????????????? ????????????????"))
        self.showStatisticFormBtn.setText(_translate("MainWindow", "???????????????? ????????????????????"))
        self.showAimsFormBtn.setText(_translate("MainWindow", "?????? ????????"))
from Pictures.Images import design


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
