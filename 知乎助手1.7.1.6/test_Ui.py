#!/usr/bin/env python
# coding=utf-8
from PyQt4 import QtCore, QtGui
from Ui import Ui_MainWindow
import sys  # 修改默认编码
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(100000) #为了适应知乎上的长答案，需要专门设下递归深度限制。。。

# 将./codes添加至库目录中
extendLibPath = r"./codes"
sys.path.append(extendLibPath)

from codes.main import *
from codes.connectSignals import *



class MyApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.writeCaptcha()
        #self.ui.label_2.setScaledContents(True)
        ##QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.fileset)
        self.ui.Login.clicked.connect(self.fileset)
        self.ui.GetVerifycode.clicked.connect(self.GetCaptcha)
        self.ui.verifycode.editingFinished.connect(self.writeCaptcha)
    def GetCaptcha(self):
        buf = urllib2.urlopen(u'http://www.zhihu.com/captcha.gif')  # 开始拉取验证码
        f = open(u'VerifyCode.gif', 'wb')
        f.write(buf.read())
        f.close()
        codename ='./VerifyCode.gif'
        image = QtGui.QImage(codename)
        pp = QtGui.QPixmap.fromImage(image)
        self.ui.verifycode_label.setPixmap(pp)
        #print u'请输入您所看到的验证码，验证码文件在助手所处的文件夹中,\n双击打开『我是登陆知乎时的验证码.gif』即可\n如果不需要输入验证码可以直接敲击回车跳过该步'
        #with open('./verifycode.txt','r') as verifycode:
           # captcha =  verifycode.read()
           # print(captcha)#raw_input()
        ##return captcha
    def writeCaptcha(self):
        verifycode = self.ui.verifycode.text()
        with open("verifycode.txt",'w') as fverifycode:
            fverifycode.write(verifycode)
    def fileset(self):
        ##mytext = self.ui.textEdit.toPlainText()
        ##mylinetext = self.ui.lineEdit.text()
        ##with open("text.txt",'a') as answer:
        ##   answer.write(mytext)
        ##  answer.write(mylinetext)
        #self.writeCaptcha()




        answers = self.ui.answers.toPlainText()
        with open("ReadList.txt",'w') as fanswers:
            fanswers.write(answers)

        mainClass = ZhihuHelp()
        mainClass.helperStart()
        pass



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    #print(verifycode)

    sys.exit(app.exec_())

