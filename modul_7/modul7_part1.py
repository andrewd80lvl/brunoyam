import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime as dt


def parse_html(url):
    print(f'Start parse_html(url): {url}')
    r = requests.get(url)
    print(r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')
    rate = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

    li_rate = list()

    for tag in rate.find_all('td'):

        if re.fullmatch(r'[*]?\d{2,4}\.\d{4}', tag.getText()):
            it_rate = tag.getText()

        elif re.fullmatch(r'[с][ ](0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d', tag.getText()):
            it_date = tag.getText().removeprefix('с ')

        elif re.fullmatch(r'[+−]\d{1,3}\.\d{1,4}', tag.getText()):
            it_delta = tag.getText()
            li_rate.append((it_rate, it_date, it_delta))

    return li_rate


def build_graph(li_rate):
    print(f'Start build_graph(rate)')

    x = []
    y = []

    for rt in li_rate:
        x.append(dt.datetime.strptime(rt[1], '%d.%m.%Y'))
        y.append(float(rt[0]))

    plt.plot(x, y)
    plt.show()

rate = parse_html("https://mfd.ru/currency/?currency=USD")
build_graph(rate)

# https://devpractice.ru/files/books/python/Matplotlib.book.pdf
