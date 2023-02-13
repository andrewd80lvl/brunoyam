import time
from threading import Thread
from datetime import datetime


def get_thread(thread_name, result, index):

    time.sleep(1)
    result[index] = thread_name + str(index)
    print("Thread name:" + result[index] + '\n')


results = [None] * 10
threads = [Thread(target=get_thread, args=("Hello", results, i)) for i in range(10)]

t2 = datetime.now()

for t in threads:
    t.start()

for t in threads:
    t.join()

print(results)


print('time ', (datetime.now() - t2).microseconds)  # level 2

# Вывод:
# Thread name:Hello8
# Thread name:Hello4
# Thread name:Hello9
# Thread name:Hello5
# Thread name:Hello7
# Thread name:Hello6
# Thread name:Hello1
# Thread name:Hello0
# Thread name:Hello2
# Thread name:Hello3
#
# ['Hello0', 'Hello1', 'Hello2', 'Hello3', 'Hello4', 'Hello5', 'Hello6', 'Hello7', 'Hello8', 'Hello9']
# time  14889

