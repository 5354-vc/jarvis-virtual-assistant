# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(1714, 914)
        self.label = QtWidgets.QLabel(jarvisUi)
        self.label.setGeometry(QtCore.QRect(0, -10, 1731, 931))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:\MCA (AL & ML)\J.A.R.V.I.S-main\J.A.R.V.I.S-main\jarvis\jarvis1.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(jarvisUi)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 411, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:\MCA (AL & ML)\J.A.R.V.I.S-main\J.A.R.V.I.S-main\jarvis\jarvis2.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(jarvisUi)
        self.label_3.setGeometry(QtCore.QRect(30, 390, 311, 471))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("E:\MCA (AL & ML)\J.A.R.V.I.S-main\J.A.R.V.I.S-main\jarvis\jarvis3.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(jarvisUi)
        self.label_4.setGeometry(QtCore.QRect(1370, 260, 391, 371))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("E:\MCA (AL & ML)\J.A.R.V.I.S-main\J.A.R.V.I.S-main\jarvis\wallpaper1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(jarvisUi)
        self.label_5.setGeometry(QtCore.QRect(1280, 40, 201, 71))
        self.label_5.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:30px")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(jarvisUi)
        self.label_7.setGeometry(QtCore.QRect(1480, 40, 201, 71))
        self.label_7.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:30px")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(jarvisUi)
        self.pushButton.setGeometry(QtCore.QRect(1350, 750, 161, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(85, 176, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(jarvisUi)
        self.pushButton_2.setGeometry(QtCore.QRect(1530, 750, 151, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 49, 76);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "Dialog"))
        self.pushButton.setText(_translate("jarvisUi", "RUN"))
        self.pushButton_2.setText(_translate("jarvisUi", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QDialog()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
