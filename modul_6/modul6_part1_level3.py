from threading import Thread
import requests
from datetime import datetime


def get_html(url):
    print(f'Start: {url}')
    r = requests.get(url)
    print(r.status_code)
    print(len(r.text))
    return r.text


urls = ['https://google.ru', 'http://info.cern.ch', 'https://ya.ru', 'http://lib.ru', 'https://www.evening-kazan.ru']

t1 = datetime.now()

for i in urls:
    get_html(i)

print('time step by step', (datetime.now() - t1).microseconds)

threads = [Thread(target=get_html, args=(url,)) for url in urls]

t2 = datetime.now()

for t in threads:
    t.start()

for t in threads:
    t.join()

print('time parallel', (datetime.now() - t2).microseconds)

#Вывод
#Start: https://google.ru
#Start: http://info.cern.ch
#Start: https://ya.ru
#Start: http://lib.ru
#Start: https://www.evening-kazan.ru
#time step by step 909896
#Start: https://google.ru
#Start: http://info.cern.ch
#Start: https://ya.ru
#Start: http://lib.ru
#Start: https://www.evening-kazan.ru
#time parallel 510370