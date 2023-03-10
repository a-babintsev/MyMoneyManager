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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 811, 611))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/money_background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.aimChgNameEdit = QtWidgets.QLineEdit(self.frame_2)
        self.aimChgNameEdit.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.aimChgNameEdit.setObjectName("aimChgNameEdit")
        self.verticalLayout.addWidget(self.aimChgNameEdit)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.aimChgSumEdit = QtWidgets.QLineEdit(self.frame_3)
        self.aimChgSumEdit.setStyleSheet("QLineEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.aimChgSumEdit.setObjectName("aimChgSumEdit")
        self.verticalLayout_2.addWidget(self.aimChgSumEdit)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setStyleSheet("color: rgb(255,255,255);\n"
"background: rgb(120, 183, 140);\n"
"font: 20px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.aimChgDateEdit = QtWidgets.QDateEdit(self.frame_4)
        self.aimChgDateEdit.setStyleSheet("QDateEdit {\n"
"    padding: 5px;\n"
"    border: 2px solid rgb(120, 183, 140);;\n"
"    border-radius: 10px;\n"
"    font: 17px;\n"
"}\n"
"\n"
"QDateEdit::hover {\n"
"    border: 2px solid rgb(120, 155, 140);\n"
"}")
        self.aimChgDateEdit.setObjectName("aimChgDateEdit")
        self.verticalLayout_3.addWidget(self.aimChgDateEdit)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoLbl = QtWidgets.QLabel(self.frame_5)
        self.infoLbl.setEnabled(True)
        self.infoLbl.setStyleSheet("color: white;\n"
"background-color: rgb(44, 153, 255);\n"
"font: 15px;\n"
"padding: 5px;\n"
"border-radius: 10px;\n"
"font-weight: bold;")
        self.infoLbl.setObjectName("infoLbl")
        self.horizontalLayout.addWidget(self.infoLbl)
        self.cancelRedactBtn = QtWidgets.QPushButton(self.frame_5)
        self.cancelRedactBtn.setStyleSheet("QPushButton#cancelRedactBtn {\n"
"     color: rgb(255, 255, 255);\n"
"    background-color: rgb(195, 0, 0);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#cancelRedactBtn:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
" }")
        self.cancelRedactBtn.setObjectName("cancelRedactBtn")
        self.horizontalLayout.addWidget(self.cancelRedactBtn)
        self.saveChangeBtn = QtWidgets.QPushButton(self.frame_5)
        self.saveChangeBtn.setStyleSheet("QPushButton#saveChangeBtn {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 183, 140);\n"
"    border: 1px solid #094065;\n"
"    border-radius: 19px; \n"
"    padding: 10px;\n"
"    font-size: 20px;\n"
" }\n"
" QPushButton#saveChangeBtn:hover {\n"
"     background-color: rgb(120, 170, 140);\n"
" }")
        self.saveChangeBtn.setObjectName("saveChangeBtn")
        self.horizontalLayout.addWidget(self.saveChangeBtn)
        self.verticalLayout_4.addWidget(self.frame_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????? ???????????? ????????????????"))
        self.label_4.setText(_translate("MainWindow", "???????????????? ????????"))
        self.label_5.setText(_translate("MainWindow", "?????????? ?????? ????????????????????????"))
        self.label_6.setText(_translate("MainWindow", "???????????????? ???????? ???????????????????? ????????"))
        self.infoLbl.setText(_translate("MainWindow", "???????????? ?????????????? ??????????????????!"))
        self.cancelRedactBtn.setText(_translate("MainWindow", "????????????"))
        self.saveChangeBtn.setText(_translate("MainWindow", "??????????????????"))
from Pictures.Images import design


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
