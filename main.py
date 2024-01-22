from flet import app
from flet import page
from flet import Text
from flet import icons
from flet import AppView
from flet import Dropdown
from flet import dropdown
from flet import Container
from flet import ElevatedButton

import json
from requests import get


def main(page: page) -> None:
    # configs
    key = 'https://api.binance.com/api/v3/ticker/price?symbol='

    # function to get price of the chosen cryptocurrency
    def get_result(event) -> None:
        nonlocal key
        link = key + 'BTCUSDT'\
            if drop_currency.value == 'Bitcoin(BTC)' else\
            key + 'ETHUSDT'

        data = get(link)
        data = data.json()

        result_txt.value = f'{data['symbol']} price is ${data['price']}'

        page.update()


    # app elements
    txt = Text(value='Choose cryptocurrency')
    result_txt = Text(value='')
    drop_currency = Dropdown(
        width=200,
        options=[
            dropdown.Option('Bitcoin(BTC)'),
            dropdown.Option('Ethereum(ETH)'),
        ],
    )
    get_button = ElevatedButton(text='get price',
                                icon=icons.AIRPLANE_TICKET,
                                on_click=get_result)

    page.add(txt, drop_currency, get_button, result_txt)


if __name__ == '__main__':
    app(target=main,
        name='Cryptocurrency watchdog',
        view=AppView.WEB_BROWSER)