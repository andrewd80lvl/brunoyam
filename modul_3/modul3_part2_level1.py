# level 1

l = [1,4,1,6,"hello","a",5,"hello"]

l_repeat = [] # повторяющиеся элементы
count = 0 #счетчик повторений
for i in l:
        for j in l:
                if i == j:
                        count += 1 #увеличиваем счетчик повторений
                        print("i:",i," count:",count) #Отладка
        if (count > 1) and (i not in l_repeat): # повторяющийся элемент списка
                l_repeat.append(i)
        
        count = 0 # Обнуляем счетчик повторений

print(l_repeat)



        


