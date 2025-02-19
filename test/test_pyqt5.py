import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建 QML 引擎
    engine = QQmlApplicationEngine()
    engine.load("./resources/ui.qml")  # 加载 QML 界面

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())  # 运行应用
