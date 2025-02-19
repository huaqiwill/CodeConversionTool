from PySide6.QtWidgets import QToolBox, QVBoxLayout, QPushButton, QWidget

class ToolBox(QToolBox):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(150)
        
        # 编码解码页
        self.codec_page = QWidget()
        codec_layout = QVBoxLayout(self.codec_page)
        self.addItem(self.codec_page, "编码解码")
        
        # 加密解密页
        self.crypto_page = QWidget()
        crypto_layout = QVBoxLayout(self.crypto_page)
        self.addItem(self.crypto_page, "加密解密")
        
        # 插件页
        self.plugin_page = QWidget()
        plugin_layout = QVBoxLayout(self.plugin_page)
        self.addItem(self.plugin_page, "插件")