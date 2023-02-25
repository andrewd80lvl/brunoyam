from threading import Thread

def foo(bar, result, index):
    print('hello')
    result[index] = "foo" + str(index)

threads = [None] * 10
results = [None] * 10

for i in range(len(threads)):
    threads[i] = Thread(target=foo, args=('world!', results, i))
    threads[i].start()

# do some other stuff

for i in range(len(threads)):
    threads[i].join()

print(results)
