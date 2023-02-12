import time
from threading import Thread
import requests
from datetime import datetime


def print_name(name):
    th_name = str('Thread name ') + str(name)
    time.sleep(1)
    print(f'Thread name: {th_name}\n')

threads = [Thread(target=print_name, args=(i+1,)) for i in range(10)]

t2 = datetime.now()

for t in threads:
    t.start()

for t in threads:
    t.join()

print('time ', (datetime.now() - t2).microseconds) # level 2

# Thread name: Thread name 9
# Thread name: Thread name 7
# Thread name: Thread name 10
# Thread name: Thread name 3
# Thread name: Thread name 4
# Thread name: Thread name 1
# Thread name: Thread name 5
# Thread name: Thread name 2
# Thread name: Thread name 8
# Thread name: Thread name 6
#
# time  20806