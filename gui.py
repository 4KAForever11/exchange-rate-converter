from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox,
                              QFrame)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QShortcut, QKeySequence, QFont, QIcon
from currency_api import CurrencyAPI

class CurrencyConverterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("汇率转换器")
        self.setFixedSize(350, 600)
        
        # 设置窗口图标
        self.setWindowIcon(QIcon("icon.ico"))
        
        # 初始化API
        self.api = CurrencyAPI()
        self.currencies = self.api.get_currencies()
        self.currency_codes = {v: k for k, v in self.currencies.items()}
        
        # 创建主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 25, 20, 20)
        main_layout.setSpacing(15)
        
        self.setup_ui(main_layout)
        self.setup_shortcuts()
        
    def setup_shortcuts(self):
        """设置快捷键"""
        # 导入所需的常量
        from PySide6.QtCore import Qt
        
        # 创建快捷键
        shortcut = QShortcut(self)
        shortcut.setKey(QKeySequence(Qt.CTRL | Qt.SHIFT | Qt.Key_S))
        shortcut.activated.connect(self.swap_currencies)
        
        # Mac 用户的快捷键
        mac_shortcut = QShortcut(self)
        mac_shortcut.setKey(QKeySequence(Qt.META | Qt.SHIFT | Qt.Key_S))
        mac_shortcut.activated.connect(self.swap_currencies)
        
    def setup_ui(self, layout):
        # 标题部分
        title_label = QLabel("汇率转换器")
        title_label.setFont(QFont("Microsoft YaHei", 22, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)
        
        layout.addSpacing(20)
        
        # 金额输入框
        amount_frame = QFrame()
        amount_frame.setStyleSheet("""
            QLineEdit {
                padding: 8px 12px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 14px;
                min-height: 35px;
                background-color: white;
            }
            QLineEdit::placeholder {
                color: #999;
            }
        """)
        
        amount_layout = QVBoxLayout(amount_frame)
        amount_layout.setContentsMargins(0, 0, 0, 0)
        
        # 添加输入框
        self.amount_entry = QLineEdit()
        self.amount_entry.setPlaceholderText("请输入要转换的金额")
        amount_layout.addWidget(self.amount_entry)
        
        layout.addWidget(amount_frame)
        
        layout.addSpacing(10)
        
        # 从货币选择框
        from_currency_frame = QFrame()
        from_currency_frame.setStyleSheet("""
            QComboBox {
                padding: 8px 12px;
                border: 1px solid #ddd;
                border-radius: 5px;
                min-height: 35px;
                font-size: 13px;
                background-color: white;
            }
            QLabel {
                font-size: 14px;
                margin-right: 5px;
            }
        """)
        
        from_layout = QHBoxLayout(from_currency_frame)
        from_layout.setContentsMargins(0, 5, 0, 5)
        from_label = QLabel("从:")
        from_label.setFixedWidth(25)
        from_label.setFont(QFont("Microsoft YaHei", 10))
        self.from_currency = QComboBox()
        self.from_currency.addItems(self.currencies.values())
        self.from_currency.setCurrentText(self.currencies["USD"])
        from_layout.addWidget(from_label)
        from_layout.addWidget(self.from_currency)
        
        layout.addWidget(from_currency_frame)
        
        # 交换按钮
        swap_frame = QFrame()
        swap_btn = QPushButton("⇅")
        swap_btn.setFixedSize(QSize(28, 28))
        swap_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 14px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        swap_btn.clicked.connect(self.swap_currencies)
        
        swap_layout = QHBoxLayout(swap_frame)
        swap_layout.setContentsMargins(0, 2, 15, 2)
        swap_layout.addStretch()
        swap_layout.addWidget(swap_btn)
        
        layout.addWidget(swap_frame)
        
        # 到货币选择框
        to_currency_frame = QFrame()
        to_currency_frame.setStyleSheet("""
            QComboBox {
                padding: 8px 12px;
                border: 1px solid #ddd;
                border-radius: 5px;
                min-height: 35px;
                font-size: 13px;
                background-color: white;
            }
            QLabel {
                font-size: 14px;
                margin-right: 5px;
            }
        """)
        
        to_layout = QHBoxLayout(to_currency_frame)
        to_layout.setContentsMargins(0, 5, 0, 5)
        to_label = QLabel("到:")
        to_label.setFixedWidth(25)
        to_label.setFont(QFont("Microsoft YaHei", 10))
        self.to_currency = QComboBox()
        self.to_currency.addItems(self.currencies.values())
        self.to_currency.setCurrentText(self.currencies["CNY"])
        to_layout.addWidget(to_label)
        to_layout.addWidget(self.to_currency)
        
        layout.addWidget(to_currency_frame)
        
        layout.addSpacing(10)
        
        # 转换按钮
        convert_btn = QPushButton("转换")
        convert_btn.setFixedHeight(38)
        convert_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        convert_btn.clicked.connect(self.convert)
        layout.addWidget(convert_btn)
        
        # 结果显示
        result_frame = QFrame()
        result_frame.setStyleSheet("""
            QLabel {
                font-size: 13px;
                color: #333;
                padding: 10px 0;
            }
        """)
        
        result_layout = QVBoxLayout(result_frame)
        result_layout.setContentsMargins(0, 5, 0, 5)
        
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Microsoft YaHei", 12))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setWordWrap(True)
        result_layout.addWidget(self.result_label)
        
        layout.addWidget(result_frame)
        
        # 快捷键提示
        shortcut_label = QLabel("快捷键: Ctrl+Shift+S 切换货币")
        shortcut_label.setFont(QFont("Microsoft YaHei", 9))
        shortcut_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        shortcut_label.setStyleSheet("""
            color: #666;
            margin-top: 10px;
            padding: 5px;
        """)
        layout.addWidget(shortcut_label)
        
    def swap_currencies(self):
        """交换两个货币选择框的值"""
        from_value = self.from_currency.currentText()
        to_value = self.to_currency.currentText()
        self.from_currency.setCurrentText(to_value)
        self.to_currency.setCurrentText(from_value)
        # 移除自动转换功能
        # if self.amount_entry.text().strip():
        #     self.convert()
    
    def get_currency_code(self, display_text):
        return self.currency_codes[display_text]
        
    def convert(self):
        try:
            amount = float(self.amount_entry.text())
            from_curr_display = self.from_currency.currentText()
            to_curr_display = self.to_currency.currentText()
            
            from_curr = self.get_currency_code(from_curr_display)
            to_curr = self.get_currency_code(to_curr_display)
            
            result = self.api.convert_currency(from_curr, to_curr, amount)
            
            if result is not None:
                self.result_label.setText(
                    f"{amount:.2f} {self.currencies[from_curr]} = {result:.2f} {self.currencies[to_curr]}"
                )
            else:
                QMessageBox.critical(self, "错误", "转换失败,稍后重试")
                
        except ValueError:
            QMessageBox.critical(self, "错误", "请输入有效的数字金额") 