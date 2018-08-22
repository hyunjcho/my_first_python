from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint

cc = ForeignExchange(key='AS0C1JP1LQY65GBK')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='USD',to_currency='KRW')
pprint(data)
