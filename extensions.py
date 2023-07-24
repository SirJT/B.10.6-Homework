import requests
import json

from config import keys

class APIExeptions(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIExeptions(f'Невозможно перевести одинаковые валюты{base}')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise APIExeptions(f'Невозможно обработать валюту {quote}')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIExeptions(f'Невозможно обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeptions(f'Невозможно обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]] * float(amount)
        return total_base