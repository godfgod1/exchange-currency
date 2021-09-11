import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency




country_info_url = "https://www.iban.com/currency-codes"


def save_countries_info():
  print('Welcome to a CurrencyConvert PRO 2021 by Sungwoo\n ')
  arr = []
  num = 0
  request = requests.get(country_info_url)
  soup = BeautifulSoup(request.text,
  'html.parser')
  table = soup.find('table',{"class":'table'})
  tbody = table.find('tbody')
  trs = tbody.find_all('tr')
  for tr in trs:
    country = tr.contents[1].string
    code = tr.contents[5].string
    if code == None:
      continue
    
    arr.append({'num':f"{num}",'country':country,'code':code})
    num += 1
  
  for i in arr:
    print(f"# {i['num']} {i['country']}")
  
  print('\nWhere are you from ? Choose a country by number.' )

  return arr


def exchange_money(countries_info):
  exchange = []
  code ={}
  try:
    my_country_num = int(input('#: '))
    for i in countries_info:
      if my_country_num == int(i['num']):
        print(i['country'])
        code['country'] = i['country']
        code['code'] = i['code']
        exchange.append(code)
        another_country(countries_info, exchange)
  except:
    print("That' was not a number")
    return exchange_money(countries_info)

def another_country(countries_info,exchange):
  code = {}
  print('\nNow choose another country')
  try:
    anthoer_country_num = int(input('#: '))
    for i in countries_info:
      if anthoer_country_num == int(i['num']):
        print(i['country'])
        code['country'] = i['country']
        code['code'] = i['code']
        exchange.append(code)
        excute_exchange_money(exchange)
  except:
    print("That' was not a number")
    return another_country(countries_info,exchange)

def excute_exchange_money(exchange):
  
  print(f'\nHow many {exchange[0]["code"]} do you want to convert to {exchange[1]["code"]}?')
  my_currency = exchange[0]['code']
  another_currency = exchange[1]['code']

  try:
    input_amount = int(input(""))
  
    request = requests.get(f'https://wise.com/gb/currency-converter/{my_currency}-to-{another_currency}-rate?amount={input_amount}')
    soup = BeautifulSoup(request.text,
  'html.parser')
    calculator = soup.find('div',{'class':'cc-calculator__rate'})
    another_currency_rate = calculator.find('span',{"class":'text-success'}).get_text()
    another_currency_rate = float(another_currency_rate)
    
    result = input_amount * another_currency_rate
    mine = format_currency(input_amount, my_currency, locale="ko_KR")
    another = format_currency(result, another_currency, locale="ko_KR")

    print(f"{mine} is {another}")
    return 
  except:
    print("That' was not a number")
    return excute_exchange_money(exchange)

