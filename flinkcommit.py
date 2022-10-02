# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flinkcommit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import flinkcommitdb as commitdb
import flinkpost
import hdfsupload


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("FlinkCommit")
        Dialog.resize(897, 604)
        self.allname = None
        self.params = None
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(490, 460, 341, 101))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.jar = QtWidgets.QComboBox(Dialog)
        self.jar.setGeometry(QtCore.QRect(140, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.jar.setFont(font)
        self.jar.setObjectName("jar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 110, 41, 16))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 54, 12))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.classentry = QtWidgets.QComboBox(Dialog)
        self.classentry.setGeometry(QtCore.QRect(140, 150, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.classentry.setFont(font)
        self.classentry.setObjectName("classentry")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.startyarnsession = QtWidgets.QPushButton(Dialog)
        self.startyarnsession.setGeometry(QtCore.QRect(710, 420, 101, 31))
        self.startyarnsession.setObjectName("startyarnsession")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 340, 301, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 54, 12))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.jobmodel = QtWidgets.QComboBox(Dialog)
        self.jobmodel.setGeometry(QtCore.QRect(140, 190, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.jobmodel.setFont(font)
        self.jobmodel.setObjectName("jobmodel")
        self.jobmodel.addItem("")
        self.jobmodel.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(70, 360, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 390, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 430, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.processmem = QtWidgets.QLineEdit(Dialog)
        self.processmem.setGeometry(QtCore.QRect(310, 350, 113, 20))
        self.processmem.setObjectName("processmem")
        self.managedmem = QtWidgets.QLineEdit(Dialog)
        self.managedmem.setGeometry(QtCore.QRect(310, 390, 113, 20))
        self.managedmem.setObjectName("managedmem")
        self.slotnum = QtWidgets.QLineEdit(Dialog)
        self.slotnum.setGeometry(QtCore.QRect(310, 430, 113, 20))
        self.slotnum.setObjectName("slotnum")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 310, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 300, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(510, 410, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(70, 470, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 510, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(310, 470, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 510, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(510, 490, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(480, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setFont(font)
        self.textBrowser.setGeometry(QtCore.QRect(480, 100, 371, 221))
        self.textBrowser.setObjectName("textBrowser")

        # 关联操作
        self.retranslateUi(Dialog)
        self.selectJar()
        # jar
        self.jar.currentIndexChanged.connect(self.selectClass)
        self.jar.currentIndexChanged.connect(self.getapi)
        # class
        self.classentry.currentIndexChanged.connect(self.selectAllName)
        self.classentry.currentIndexChanged.connect(self.getapi)
        # model
        self.jobmodel.currentIndexChanged.connect(self.getapi)
        # fromck
        self.comboBox.currentIndexChanged.connect(self.getapi)
        # taskprocessmem
        self.processmem.textChanged.connect(self.getapi)
        # taskmamaged.size
        self.managedmem.textChanged.connect(self.getapi)
        # slotnum
        self.slotnum.textChanged.connect(self.getapi)
        # jobheap
        self.lineEdit.textChanged.connect(self.getapi)
        # joboffheap
        self.lineEdit_2.textChanged.connect(self.getapi)

        self.pushButton.clicked.connect(self.upLoad)
        # self.buttonBox.accepted.connect(Dialog.accept)
        self.startyarnsession.clicked.connect(self.startYarn)
        self.buttonBox.accepted.connect(self.showMess)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.rejected.connect(self.exit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FlinkCommit"))
        self.label.setText(_translate("Dialog", "Jar："))
        self.label_2.setText(_translate("Dialog", "Class："))
        self.label_3.setText(_translate("Dialog", "基础配置："))
        self.startyarnsession.setText(_translate("Dialog", "YarnSession"))
        self.label_4.setText(_translate("Dialog", "Model:"))
        self.jobmodel.setItemText(0, _translate("Dialog", "yarn-session"))
        self.jobmodel.setItemText(1, _translate("Dialog", "yarn-per-job"))
        self.label_5.setText(_translate("Dialog", "高级配置："))
        self.label_6.setText(_translate("Dialog", "taskmanager.memory.process.size    ："))
        self.label_7.setText(_translate("Dialog", "taskmanager.memory.managed.size ："))
        self.label_8.setText(_translate("Dialog", "taskmanager.number.taskslots           ："))
        self.label_9.setText(_translate("Dialog", "fromck:"))
        self.comboBox.setItemText(0, _translate("Dialog", "no"))
        self.comboBox.setItemText(1, _translate("Dialog", "yes"))
        self.label_10.setText(_translate("Dialog", "启动yarn-session容器："))
        self.label_11.setText(_translate("Dialog", "jobmanager.memory.heap.size            ："))
        self.label_12.setText(_translate("Dialog", "jobmanager.memory.off-heap.size     ："))
        self.label_13.setText(_translate("Dialog", "提交任务："))
        self.label_14.setText(_translate("Dialog", "PostJson："))
        self.pushButton.setText(_translate("Dialog", "上传Jar包"))

    def showMess(self):
        if self.params == None:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请先输入信息！！')
        else:
            res = flinkpost.flinkpost(self.params)
            msg_box = QMessageBox(QMessageBox.Information, '执行结果', res)
        msg_box.exec_()
        return

    def startYarn(self):
        params = {
            'model': "yarn"
        }
        res = flinkpost.flinkpost(params)
        msg_box = QMessageBox(QMessageBox.Information, '执行结果', res)
        msg_box.exec_()

    def upLoad(self):
        try:
            url = QFileDialog.getOpenFileNames(None, "请选择要上传的文件", r"D:\\", "Jar(*.jar);;All Files(*)")
            hdfsupload.hdfsupload(url[0][0])
            conf = {'dwonpath':url[0][0]}
            flinkdown = flinkpost.flinkdown(conf)
            # hdfscheck = hdfsupload.hdfscheck(url[0][0])
            msg_box = QMessageBox(QMessageBox.Information, '执行结果', flinkdown)
            msg_box.exec_()
        except:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '上传失败')
            msg_box.exec_()
        return

    def exit(self):
        QMessageBox.about(None, "作者@Putin", "欢迎下次光临🙂")
        return

    def selectJar(self):
        _translate = QtCore.QCoreApplication.translate
        self.jar.addItem("")
        getjars = commitdb.FLINKCOMMITDB().getjars()
        for i in range(0, len(getjars)):
            self.jar.addItem(_translate("Dialog", getjars[i][0]))
        return

    def selectClass(self):
        self.classentry.clear()
        _translate = QtCore.QCoreApplication.translate
        jar = self.jar.currentText()
        get_class = commitdb.FLINKCOMMITDB().getClass(jar)
        for i in range(0, len(get_class)):
            self.classentry.addItem(_translate("Dialog", get_class[i][0]))
        return

    def selectAllName(self):
        jar = self.jar.currentText()
        classentry = self.classentry.currentText()
        self.allname = commitdb.FLINKCOMMITDB().getAllName(jar, classentry)
        return

    def getapi(self):
        _translate = QtCore.QCoreApplication.translate
        jar = self.jar.currentText()
        classentry = self.classentry.currentText()
        params = {}
        if jar != "" and classentry != "":
            params["jar"] = jar
            params["classentry"] = classentry
            params["model"] = self.jobmodel.currentText()
            if self.jobmodel.currentText() == "yarn-per-job":
                params["appname"] = self.allname[0][0]
                if self.processmem.text() != "":
                    params["taskprocess"] = self.processmem.text()
                if self.managedmem.text() != "":
                    params["taskmem"] = self.managedmem.text()
                if self.slotnum.text() != "":
                    params["slotnum"] = self.slotnum.text()
                if self.lineEdit.text() != "":
                    params["jbheap"] = self.lineEdit.text()
                if self.lineEdit_2.text() != "":
                    params["jboffheap"] = self.lineEdit_2.text()

            params["fromck"] = self.comboBox.currentText()
            if self.comboBox.currentText() == "yes":
                params["ckname"] = self.allname[0][1]
            self.textBrowser.setText(json.dumps(params, indent=1))
            self.params = params
        else:
            self.textBrowser.clear()
            self.params = None
        return


if __name__ == "__main__":
    mypro = QtWidgets.QApplication(sys.argv)
    mywin = QtWidgets.QDialog()
    thisui = Ui_Dialog()
    thisui.setupUi(mywin)
    mywin.show()
    sys.exit(mypro.exec_())
