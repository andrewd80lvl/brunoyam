d = {'name1':'id1','name2':'id2','name3': 'id3','name4': 'id3','name5': 4}

print(d)

c = dict() # Словарь 
for key, value in d.items():
	if value is not c.keys(): # Проверяем уникальность ключей (c 'id3' проверка не срабатывает?)
		c[value] = key
		print(c.keys()) 
	else:
		print("Ключ ", value, "уже существует") 

print(c) # выводим словарь 'c' c замененными значениями key, value

#Вариант 2 - похоже нельзя словарь d
#for i in d.keys():
# 	value = d.pop(i)
# 	d[value] = key
# 	print(i)

# print(d) # выводим словарь 'd' c замененными значениями key, value




