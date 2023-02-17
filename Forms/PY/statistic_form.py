from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 690)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/dollar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 691))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Pictures/money_background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 290, 801, 411))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.statisticTable = QtWidgets.QTableWidget(self.frame_3)
        self.statisticTable.setObjectName("statisticTable")
        self.statisticTable.setColumnCount(0)
        self.statisticTable.setRowCount(0)
        self.verticalLayout_2.addWidget(self.statisticTable)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultLbl = QtWidgets.QLabel(self.frame_4)
        self.resultLbl.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid #094065;\n"
"border-radius: 19px; \n"
"background-color: rgb(0, 179, 255);\n"
"padding: 10px;\n"
"font-size: 20px;\n"
"")
        self.resultLbl.setText("")
        self.resultLbl.setObjectName("resultLbl")
        self.horizontalLayout.addWidget(self.resultLbl)
        self.backMenuBtn = QtWidgets.QPushButton(self.frame_4)
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
        self.horizontalLayout.addWidget(self.backMenuBtn)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_3)
        self.diagram_frame = QtWidgets.QFrame(self.frame)
        self.diagram_frame.setGeometry(QtCore.QRect(-1, -1, 801, 291))
        self.diagram_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diagram_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diagram_frame.setObjectName("diagram_frame")
        self.MplWidget = MplWidget(self.diagram_frame)
        self.MplWidget.setGeometry(QtCore.QRect(-1, -1, 811, 291))
        self.MplWidget.setObjectName("MplWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учёт личных финансов"))
        self.backMenuBtn.setText(_translate("MainWindow", "Назад"))
from Windows.Utils.mplwidget import MplWidget
from Pictures.Images import statistic_resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
