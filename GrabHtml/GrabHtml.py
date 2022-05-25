import Configure.configure as config
import requests as rq
from bs4 import BeautifulSoup


def get_html():
    url = config.GRAB_HTML
    html_header = config.HTML_HEADER
    r = rq.get(url, headers=html_header)
    html_str = r.text
    soup = BeautifulSoup(html_str, "lxml")
    search_coin = ['eth', 'trx']
    coin_data = []
    for coin in search_coin:
        data_coin_symbol = soup.find('span', {'data-coin-symbol': '{coin}'.format(coin=coin)})
        coin_data.append(data_coin_symbol)
    print(coin_data)


if __name__ == '__main__':
    get_html()
