# 汇率转换器 (Exchange Rate Converter)

一个简洁美观的汇率转换工具，基于 Python 和 PySide6 开发。支持全球主要货币之间的实时汇率转换。

![程序截图](screenshots/main.png)

## 功能特点

- 支持30多种主要货币的转换
- 实时获取最新汇率数据
- 简洁直观的用户界面
- 支持快捷键操作
- 支持货币快速切换


## 项目结构

```
exchange-rate-converter/
├── run.py # 程序入口
├── gui.py # 图形界面实现
├── currency_api.py # 汇率API接口
├── icon.ico # 程序图标
├── converter.spec # PyInstaller配置文件
└── requirements.txt # 项目依赖
```

## 技术栈

- Python 3.8+
- PySide6 (Qt for Python)
- Requests
- PyInstaller

## 安装使用

### 方式一：直接运行可执行文件

1. 从 [Releases](https://github.com/yourusername/exchange-rate-converter/releases) 页面下载最新版本
2. 解压后双击运行 `汇率转换器.exe`

### 方式二：从源码运行

1. 克隆仓库 
```bash
git clone https://github.com/yourusername/exchange-rate-converter.git

cd exchange-rate-converter
```


2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行程序
```bash
python run.py
``` 


## API 说明

本项目使用 [currencyapi](https://currencyapi.com/) 提供的免费汇率 API。


## 开发说明

### 环境要求

- Python 3.8 或更高版本
- pip 包管理器


## 贡献指南

欢迎提交 Pull Request 或创建 Issue。

## 作者

- [@4KAForever11](https://github.com/4KAForever11)

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 致谢

- [currencyapi](https://currencyapi.com/) - 提供免费汇率 API
- [PySide6](https://wiki.qt.io/Qt_for_Python) - 提供 GUI 框架
