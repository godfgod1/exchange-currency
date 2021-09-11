import os
from babel.numbers import format_currency
from exchange import save_countries_info,exchange_money

os.system("clear")
url = "https://www.iban.com/currency-codes"

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""





save_countries_info = save_countries_info()
exchange_money = exchange_money(save_countries_info)
exchange_money


# print(format_currency(5000, "KRW", locale="ko_KR"))






