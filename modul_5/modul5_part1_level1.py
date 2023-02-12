
class StringVar:
    def __init__(self, data):
        self.__string = data

    def set(self,data):
        self.__string = data

    def get(self):
        return self.__string

    def __add__(self, other):
        if isinstance(other, str) == True:
            self.__string += other

        return StringVar(self.__string)

test = StringVar("Текст")
print(test.get())

test.set("Новая строка")

print(test.get())
new = str(" с текстом")

test = test + new
print(test.get())

