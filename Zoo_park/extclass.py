import requests
import json
from data import questions, TOKEN

class APIException(Exception):
    pass

class CriptoConvert():
    @staticmethod
    def obrabotka(values, questions):
        try:
            if not values.isnumeric():
                raise APIException('Ошибка ввода')
        except:
            raise APIException('Неверный ввод')
        try:
            if int(values) != len(questions[1]):
                raise APIException('Веденое число не соотвествует вопросу')
        except:
            raise APIException('Неверный ввод')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_t}&tsyms={base_t}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
