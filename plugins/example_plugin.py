from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from .base_plugin import BasePlugin

class ExamplePlugin(BasePlugin):
    def name(self) -> str:
        return "示例插件"
    
    def description(self) -> str:
        return "这是一个示例插件"
    
    def get_widget(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("这是示例插件的界面"))
        return widget