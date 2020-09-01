import pandas as pd
url = 'http://www.stockq.org/market/currency.php'
currencys = pd.read_html(url)

currency = currencys[7]
currency = currency.drop(currency.index[[0,1]])
currency.columns = ['貨幣','匯率','漲跌','比例','台北']
currency.index = range(len(currency.index))
print(currency)