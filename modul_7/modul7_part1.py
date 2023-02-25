import requests
from bs4 import BeautifulSoup


def parse_html(url):
    print(f'Start: {url}')
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text,'html.parser')

    rate = soup.find('table',{'class': 'mfd-table mfd-currency-table'})

    for tag in rate.find_all('td'):
        print(tag.getText())



    return r.text


parse_html("https://mfd.ru/currency/?currency=USD")
