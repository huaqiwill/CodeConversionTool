from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from ..components.tab_widget import MainTabWidget
from ..components.tool_box import ToolBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("编码转换工具")
        self.setMinimumSize(800, 600)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 创建主要的标签页组件
        self.tab_widget = MainTabWidget()
        
        # 创建工具箱
        self.tool_box = ToolBox()
        
        # 添加组件到布局
        layout.addWidget(self.tool_box)
        layout.addWidget(self.tab_widget)