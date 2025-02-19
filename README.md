# CodeConversionTool 基于PyQt5的编码解码工具

一款CTF编码、解码、加密、解密工具。

## 开发灵感

* Ghost-Downloader-3
* CTF-Tools

移除一些可能并不常用的编码功能

这将是我第一个使用Python开发的开源项目，也是我第一个使用Python开发的开源项目，我之前对Python进行界面开发持怀疑态度，我认为Python很难开发出优秀的桌面程序，通过测试，我发现打开速度很快，所以决定开发一款加密解密工具，
参考Ghost-Downloader-3的目录结构和README文件，

其实我在很早之前就接触过了PyQt5和QtFluentWidget，但是一直没有时间来开发一款程序，这次我决定使用PyQt5和QtFluentWidget来开发一款加密解密工具，我之前对Python进行界面开发持怀疑态度，我认为Python很难开发出优秀的桌面程序，通过测试，我发现打开速度很快，所以决定开发一款加密解密工具，

使用PyQt5结合QtFluentWidgets开发界面，参考CTF-Tools项目。完成开发。
参考Ghost-Downloader-3目录结构和技术体系开发界面和功能。

CTF-Tools菜单：
菜单：常见编码、常见解码、Base编码，Base解码，加密，解密，进制转换，字符处理，在线工具，插件，其他
按钮：粘贴，复制，清空，增加Tab，现代密码，复制，清空，转源文本，密文分析，提取Flag
界面：源文本编辑框，结果文本编辑框
功能：支持多Tab，
参考精易编程助手编码解码界面。

## 创新点

由于CTF-Tools界面老，并且打开程序比较耗时，
基于QtFluentWidgets开发界面，参考Ghost-Downloader-3目录结构和技术体系开发界面和功能。
添加动画效果，优化界面性能。

我之前对Python进行界面开发持怀疑态度，我认为Python很难开发出优秀的桌面程序，通过测试，我发现打开速度很快，所以决定开发一款加密解密工具，

# 阿波罗文本加密工具

## 阿波罗文本加密工具的功能

文本base64编码、解码

文本md5加密

文本sha1加密

...

## 界面设计

![image-20231102221719451](README.assets/image-20231102221719451.png)

## 界面分析

* 多行文本框两个：源编辑框(src_edit)，目标编辑框（dst_edit）
* 操作组合框：选择编码...
* 编码按钮，编码按钮（encode_btn）解码（decode_btn）交换（exchange_btn）


## 功能

* 加解密、编码转换小工具，base64/url编码/时间戳转换等
* 支持多行输入，自动换行
* 支持复制到剪贴板
* 支持粘贴到输入框
* 支持自动换行
* 支持自动复制到剪贴板
* 支持自动清空输入框
* 支持自动清空输出框
* 支持自动清空剪贴板
* 支持自动清空历史记录
* 支持自动清空所有内容
* 支持自动保存历史记录
* 支持自动保存所有内容


- Base64
- url编码
- 16进制（\x格式）


- timestamp
- 16进制（3B 2D格式，不区分大小写，空格可有可无）
"# CodeConversionTool" 



常见编码：
* Base64编码，Base64解码
* URL编码，URL解码
* 16进制编码，16进制解码
* 时间戳转换，时间戳转换
* Unicode编码，Unicode解码
* UTF-8编码，UTF-8解码
* GBK编码，GBK解码
* ASCII编码，ASCII解码
* ISO-8859-1编码，ISO-8859-1解码
* UTF-16编码，UTF-16解码
* UTF-32编码，UTF-32解码
* GB2312编码，GB2312解码
* GB18030编码，GB18030解码
* Big5编码，Big5解码
* Shift-JIS编码，Shift-JIS解码
* EUC-JP编码，EUC-JP解码
* EUC-KR编码，EUC-KR解码
* KOI8-R编码，KOI8-R解码
* KOI8-U编码，KOI8-U解码
* TIS-620编码，TIS-620解码
* Windows-1250编码，Windows-1250解码
* Windows-1251编码，Windows-1251解码
* Windows-1252编码，Windows-1252解码
* Windows-1253编码，Windows-1253解码
* Windows-1254编码，Windows-1254解码
* Windows-1255编码，Windows-1255解码
* Windows-1256编码，Windows-1256解码
* Windows-1257编码，Windows-1257解码
* Windows-1258编码，Windows-1258解码
* Windows-874编码，Windows-874解码
* Windows-932编码，Windows-932解码
* Windows-936编码，Windows-936解码
* Windows-949编码，Windows-949解码