import time
from threading import Thread


def start_rocket(number):
    time.sleep(3)
    print(f'Rocket № {number} started!\n')


threads = [Thread(target=start_rocket, args=(i,)) for i in range(5)]

print(threads)

for t in threads:
    t.start()

#for t in threads:
#    t.join()
