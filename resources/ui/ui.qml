import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "QML 编码工具"


    menuBar: MenuBar {
        Menu {
            title: "编码"
            MenuItem { text: "Base64 编码" }
            MenuItem { text: "Base64 解码" }
            MenuItem { text: "URL 编码" }
            MenuItem { text: "URL 解码" }
        }
        Menu {
            title: "哈希算法"
            MenuItem { text: "MD5" }
            MenuItem { text: "SHA1" }
            MenuItem { text: "SHA256" }
        }
        Menu {
            title: "关于"
            MenuItem { text: "关于程序" }
            MenuItem { text: "官网" }
        }
    }

    ColumnLayout {
        anchors.fill: parent

        Button {
            text: "添加新标签"
            onClicked: tabView.addNewTab()
        }
        
        Button {
            text: "删除当前标签"
            onClicked: tabView.removeCurrentTab()
        }

        TabBar {
            id: tabBar
            Layout.fillWidth: true
        }
        StackLayout {
            id: tabView
            Layout.fillWidth: true
            Layout.fillHeight: true

            function addNewTab() {
                var newTab = tabComponent.createObject(tabView, { "title": "新标签" });
                tabBar.addTab(newTab.title);
                tabView.addItem(newTab);
            }

            function removeCurrentTab() {
                if (tabView.count > 0) {
                    tabBar.removeTab(tabView.currentIndex);
                    tabView.removeItem(tabView.currentItem);
                }
            }
        }
    }

    Component {
        id: tabComponent
        Item {
            property string title: "新标签"
            ColumnLayout {
                anchors.fill: parent
                spacing: 10

                Label { text: "源文本:" }
                TextArea {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 100
                }

                Label { text: "结果:" }
                TextArea {
                    Layout.fillWidth: true
                    Layout.preferredHeight: 100
                }
            }
        }
    }
}