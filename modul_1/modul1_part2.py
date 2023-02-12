print("Modul 1. Part 2")

# Level 1
a = int(input())
b = int(input())
c = int(input())

res = 0

if a == b and b == c:
	res = 3
elif a == b or a == c or c==a:
	res = 2

print("Результат:" + str(res))


# Level 2
x1 = int(input("Введите координату x1:"))
if x1 > 8 and x1 < 1: 
	print("Координата x1 введена неккоректно:" + x1)
	exit()

y1 = int(input("Введите координату y1:"))
if y1 > 8 and y1 < 1:
	print("Координата y1 введена неккоректно:" + y1)
	exit()

x2 = int(input("Введите координату x2:"))
if x2 > 8 and x2 < 1:
	print("Координата x2 введена неккоректно:" + x2)
	exit()

y2 = int(input("Введите координату y2:"))
if y2 > 8 and y2 < 1:
	print("Координата h2_Y введена неккоректно:" + h2_Y)
	exit()

if x1 == x2 and y1 != y2:
	print("YES")
elif y1 == y2 and x1 != x2:
	print("YES")
else:
	print("NO")

#Level 3

flag = False

while flag == False:
	password = str(input('Введите пароль:'))

	if len(password) >= 8 :
		if password == password.lower() or password == password.upper() :
			print("Пароль должен состоять из прописных и заглавных символов")
		else:
			flag = True #пароль удволетворяет всем требовниям
			print("Пароль удволетворяет всем требовниям")
	else:
		print("Пароль меньше 8-ми символов")





