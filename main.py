import os
from babel.numbers import format_currency
from exchange import save_countries_info,exchange_money

os.system("clear")

save_countries_info = save_countries_info()
exchange_money = exchange_money(save_countries_info)
exchange_money














