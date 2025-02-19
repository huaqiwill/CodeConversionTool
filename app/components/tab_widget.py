from PySide6.QtWidgets import QTabWidget

class MainTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        
        # 连接关闭标签的信号
        self.tabCloseRequested.connect(self.close_tab)
    
    def close_tab(self, index):
        self.removeTab(index)
    
    def add_tool_tab(self, widget, title):
        return self.addTab(widget, title)