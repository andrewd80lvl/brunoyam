
order_list = [0, 5, 10, 17, 29, 29, 34, 43, 45, 46, 47, 49, 52, 52, 55, 59, 73, 77, 89, 99]

# Бинарный поиск через рекурсивный вызов функции
def search_binary_recursion(olist,index_left,index_right,num):

	if index_left > index_right:
		return -1 # Значение в массиве не найдено

	mid = int((index_left + index_right) / 2)

	if olist[mid] == num:
		return mid
	elif olist[mid] < num:
		return search_binary_recursion(olist,mid + 1,index_right,num)
	else:
		return search_binary_recursion(olist,index_left,mid-1,num)


print(search_binary_recursion(order_list,0,19,58))
print(search_binary_recursion(order_list,0,19,47))

# Вывод программы
# -1
# 10