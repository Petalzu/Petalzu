from tqdm import trange
import time as tm
import csv
__author__ = 'ayew'
import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit


class login(QWidget):
    def __init__(self):
        super(login,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("login")
        layout = QGridLayout()
        self.setGeometry(600, 600, 400, 400)
        nameLabel = QLabel("姓名")
        self.nameLineEdit = QLineEdit(" ")
        sexLabel = QLabel("性别")
        self.sexLineEdit = QLineEdit(" ")
        emitLabel = QLabel("手机号")
        self.phoneLineEdit = QLineEdit("")
        timeLabel = QLabel("邮箱")
        self.mailEdit = QLineEdit("")
        # layout.setSpacing(10)
        layout.addWidget(nameLabel,1,0)
        layout.addWidget(self.nameLineEdit,1,1)
        layout.addWidget(sexLabel, 2, 0)
        layout.addWidget(self.sexLineEdit, 2, 1)
        layout.addWidget(emitLabel,3,0)
        layout.addWidget(self.phoneLineEdit,3,1)
        layout.addWidget(timeLabel,4,0)
        layout.addWidget(self.mailEdit,4,1)
        layout.setColumnStretch(1, 10)
        save_Btn = QPushButton('保存')
        cancle_Btn = QPushButton('取消')
        cancle_Btn.clicked.connect(QCoreApplication.quit)
        save_Btn.clicked.connect(self.addNum)
        layout.addWidget(save_Btn)
        layout.addWidget(cancle_Btn)
        self.setLayout(layout)

    def addNum(self):
        name = self.nameLineEdit.text()  # 获取文本框内容
        sex = self.sexLineEdit.text()
        phone = self.phoneLineEdit.text()
        mail = self.mailEdit.text()
        print('姓名: %s 性别: %s 手机号: %s 邮箱: %s ' % (name,sex, phone, mail))

class userchange():
    def __init__(self,FileName,PPTloc):
        self.FileName = FileName
        self.PPTloc = PPTloc

    def _pptloc_(self,FileName,read): #获得索引的工具
        with open(FileName, 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            column = [row['属性名'] for row in reader]
            self.PPTloc = column.index(read)

    def _pptnum_(self,FileName,read): #获得值的工具
        with open(FileName,'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            column = [row['属性值'] for row in reader]
            location = column.index(read)
            self.PPTloc = int(column[location])

class instance():

    def __init__(self,FileName,PPT,name,skillname,skillproperty,time,userproperty):
        self.FileName = FileName
        self.PPT = PPT

    def _changeSkill_(self,skillname,skillproperty):
        pass

    def _PPTloc1_(self,Filename,loc):
        with open(Filename, 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            column = [row['属性名'] for row in reader]
            location = column.index(read)

    def _PPTloc2_(self,Fliename,loc):
        with open(userNameFile, 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            column = [row['属性名'] for row in reader]
            location = column.index(read)

    def _proecss_(self,time):
        for i in trange(time): 
            tm.sleep(1)

