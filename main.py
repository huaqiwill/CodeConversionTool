import sys
from PySide6.QtWidgets import QApplication
from app.view.main_window import MainWindow
from app.plugins.plugin_manager import PluginManager

def main():
    app = QApplication(sys.argv)
    
    # 创建插件管理器
    # plugin_manager = PluginManager()
    # plugin_manager.load_plugins("plugins")
    
    # 创建主窗口
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()