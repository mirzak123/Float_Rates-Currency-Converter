import requests
import json


currency = input().lower()
currency_link = "http://www.floatrates.com/daily/" + currency + ".json"
currency_json_string = requests.get(currency_link).text
currency_dict = json.loads(currency_json_string)

if currency == 'usd':
    usd = {'rate': 1}
    eur = currency_dict['eur']
elif currency == 'eur':
    usd = currency_dict['usd']
    eur = {'rate': 1}
else:
    usd = currency_dict['usd']
    eur = currency_dict['eur']

exchange_rates = {'usd': usd['rate'], 'eur': eur['rate']}

while True:
    to_currency = input().lower()
    if not to_currency:
        break
    amount = float(input())
    print("Checking the cache...")
    if to_currency in exchange_rates:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        to_currency_dict = currency_dict[to_currency]
        exchange_rates[to_currency] = to_currency_dict['rate']
        exchange_amount = exchange_rates[to_currency] * amount

    exchange_amount = exchange_rates[to_currency] * amount
    print(f"You received {exchange_amount: .2f} {to_currency.upper()}.")
