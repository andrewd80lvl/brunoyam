print("Hourses")


# Ввод данных
h1_X = int(input("Введите координату X для h1:"))
if h1_X > 8 and h1_X < 1: 
	print("Координата h1_X введена неккоректно:" + h1_X)
	exit()

h1_Y = int(input("Введите координату Y для h1:"))
if h1_Y > 8 and h1_Y < 1:
	print("Координата h1_Y введена неккоректно:" + h1_Y)
	exit()

h2_X = int(input("Введите координату X для h2:"))
if h2_X > 8 and h2_X < 1:
	print("Координата h2_X введена неккоректно:" + h2_X)
	exit()

h2_Y = int(input("Введите координату Y для h2:"))
if h2_Y > 8 and h2_Y < 1:
	print("Координата h2_Y введена неккоректно:" + h2_Y)
	exit()


#Наверх
if h1_X + 1 == h2_X and h1_Y - 2 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:" + str(h2_X) + " Y:" + str(h2_Y))

elif h1_X - 1 == h2_X and h1_Y - 2 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))

#Вправо
elif h1_X + 2 == h2_X and h1_Y - 1 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))

elif h1_X + 2 == h2_X and h1_Y + 1 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))

#Вниз
elif h1_X + 1 == h2_X and h1_Y + 2 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))

elif h1_X - 1  == h2_X and h1_Y + 2 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))
	
#Влево
elif h1_X - 2 == h2_X and h1_Y + 1 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))

elif h1_X - 2  == h2_X and h1_Y - 1 == h2_Y:
	print("Кони бьют друг друга по координатам " + "X:"  + str(h2_X) + " Y:" +  str(h2_Y))
else:
	print("Кони не бьют друг друга")


