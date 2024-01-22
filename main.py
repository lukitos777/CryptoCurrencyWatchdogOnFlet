from flet import Row
from flet import app
from flet import page
from flet import Text
from flet import Image
from flet import icons
from flet import Column
from flet import AppView
from flet import Dropdown
from flet import dropdown
from flet import Container
from flet import ElevatedButton

from requests import get


def main(page: page) -> None:
    # configs
    key = 'https://api.binance.com/api/v3/ticker/price?symbol='
    src_btc = 'assets/BTC.png'
    src_eth = 'assets/ETH.png'

    # function to get price of the chosen cryptocurrency
    def get_result(event) -> None:
        nonlocal key
        link = key + 'BTCUSDT'\
            if drop_currency.value == 'Bitcoin(BTC)' else\
            key + 'ETHUSDT'

        data = get(link)
        data = data.json()

        result_txt.value =\
            f'{'Bitcoin\'s'\
                if drop_currency.value == 'Bitcoin(BTC)' else\
                'Ethereum\'s'} price is ${data['price']}'

        coin_image.src = src_btc\
            if drop_currency.value == 'Bitcoin(BTC)' else\
            src_eth

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
    coin_image = Image(width=64, height=64, src='assets/coin.png')

    # containers
    container_1 = Container(
        width=200,
        content=Column(
            controls=[
                txt,
                drop_currency,
                get_button
            ]
        )
    )
    container_2 = Container(
        width=650,
        content=Row(
            controls=[
                coin_image,
                result_txt
            ]
        ),
    )

    page.add(Row(controls=[container_1, container_2]))


if __name__ == '__main__':
    app(target=main,
        name='Cryptocurrency watchdog',
        view=AppView.WEB_BROWSER)