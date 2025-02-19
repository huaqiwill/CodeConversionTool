"""2023/11/1 PengCunfu www.pecf.com
编码转换工具
* base64编码和解码
* utf-8编码和解码
* gbk编码和解码
* 可以从一种编码转换成另外一种编码


常见的加密工具
* md5加密
* sha1加密
* 求文件的md5值
"""
import base64
import hashlib
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QComboBox, QWidget


class Encode(object):
    @staticmethod
    def encode_base64():
        pass

    @staticmethod
    def decode_base64():
        pass

    @staticmethod
    def encode_utf_8():
        pass

    @staticmethod
    def decode_utf_8():
        pass

    @staticmethod
    def decode_gbk():
        pass

    @staticmethod
    def encode_gbk():
        pass


class Password(object):
    @staticmethod
    def md5(content, encoding="utf-8"):
        m = hashlib.md5()
        m.update(content.encode(encoding))
        return m.hexdigest()

    @staticmethod
    def file_md5(file, encoding="utf-8"):
        with open(file, encoding=encoding) as f:
            return Password.md5(f.read(), encoding)

    @staticmethod
    def sha1(content: str, encoding="utf-8"):
        m = hashlib.sha1()
        m.update(content.encode(encoding))
        return m.hexdigest()


from PyQt5.QtWidgets import *


class UserPage(QMainWindow):
    def __init__(self):
        super(QMainWindow, UserPage).__init__(self)
        self.setWindowTitle("阿波罗文本加密工具")
        self.resize(600, 400)
        
        grid_layout = QGridLayout()
        
        
        encode_btn = QPushButton("编码")
        decode_btn = QPushButton("解码")
        exchange_btn = QPushButton("交换")
        
        src_edit = QTextEdit()
        dst_edit = QTextEdit()
        
        grid_layout.addWidget()
        grid_layout.setSpacing(10)
        grid_layout.addWidget(src_edit,10,10,90,90)
        grid_layout.addWidget(encode_btn)
        grid_layout.addWidget(decode_btn)
        grid_layout.addWidget(exchange_btn)
        grid_layout.addWidget(dst_edit)
        self.setLayout(grid_layout)
        
        


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    sys.exit(app.exec_())
