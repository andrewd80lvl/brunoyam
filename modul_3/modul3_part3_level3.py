from random import randrange

list_random = ["56" , "9" , "11" ,"2","98","987"]

len_list = len(list_random)

# Сравнение двух чисел
def compare_two_value(value1, value2):

	if(len(value1) > len(value2)): #Вычисляем 
		len_min = len(value2)
	else:
		len_min = len(value1)

	for i in range(len_min):
		
		if int(value1[i]) == int(value2[i]):
			continue # Прерываем итерацию цикла и продолжаем цикл в новой итерации 

		elif int(value1[i]) > int(value2[i]):
			return 1 # Возвращаем индекс большего числе
		else:
			return 2 # Возвращаем индекс большего числе

	# Тут числа по циклу равны 

	if len(value1) == len(value2):
		return 2 # Тут все равно какой  индект числа возвращать, главное минимизировать перестановки

	elif  len(value1) > len(value2):
		return 2 # Считаем что меньшее по разрадности число имеет больший вес
	else:
		return 1

#Упорядычивание списка методом "пузырька"
def order_list_bubble(list_random): 
	for i in range(len_list):
		for j in range(len_list - 1 - i):
			if compare_two_value(list_random[j],list_random[j+1]) == 2:
				# Меняем местами - пузырек всплывает (влево)
				temp = list_random[j+1]
				list_random[j+1] = list_random[j]
				list_random[j] = temp


print(list_random)

order_list_bubble(list_random) # Упорядычиваем список

print(list_random)

string_num = str()
for i in list_random:
 string_num += i

print("Максимальное число:", int(string_num))

# Вывод 
# ['56', '9', '11', '2', '98', '987']
# ['9', '98', '987', '56', '2', '11']
# Максимальное число: 99898756211