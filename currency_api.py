import requests

class CurrencyAPI:
    def __init__(self):
        self.base_url = "https://api.frankfurter.app"
        # 添加货币代码与中文名称的映射
        self.currency_names = {
            "AUD": "澳元",
            "BGN": "保加利亚列弗",
            "BRL": "巴西雷亚尔",
            "CAD": "加拿大元",
            "CHF": "瑞士法郎",
            "CNY": "人民币",
            "CZK": "捷克克朗",
            "DKK": "丹麦克朗",
            "EUR": "欧元",
            "GBP": "英镑",
            "HKD": "港币",
            "HUF": "匈牙利福林",
            "IDR": "印尼盾",
            "ILS": "以色列新谢克尔",
            "INR": "印度卢比",
            "ISK": "冰岛克朗",
            "JPY": "日元",
            "KRW": "韩元",
            "MXN": "墨西哥比索",
            "MYR": "马来西亚林吉特",
            "NOK": "挪威克朗",
            "NZD": "新西兰元",
            "PHP": "菲律宾比索",
            "PLN": "波兰兹罗提",
            "RON": "罗马尼亚列伊",
            "SEK": "瑞典克朗",
            "SGD": "新加坡元",
            "THB": "泰铢",
            "TRY": "土耳其里拉",
            "USD": "美元",
            "ZAR": "南非兰特"
        }
        
    def get_currencies(self):
        """获取所有支持的货币代码"""
        response = requests.get(f"{self.base_url}/currencies")
        if response.status_code == 200:
            currencies = response.json()
            # 返回代码和中文名称的映射
            return {code: f"{self.currency_names.get(code, code)} ({code})" 
                   for code in currencies.keys()}
        return None
        
    def convert_currency(self, from_currency, to_currency, amount):
        """转换货币"""
        url = f"{self.base_url}/latest"
        params = {
            "amount": amount,
            "from": from_currency,
            "to": to_currency
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["rates"][to_currency]
        return None 