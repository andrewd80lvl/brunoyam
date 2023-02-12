# level 3
num = str(input("Введите число:"))

sum_rank = 0 # Сумма цифр в числе
for i in range(len(num)):
    if num[i].isdigit():
        sum_rank += int(num[i])
    else:
        print("Символ:",num[i]," не является числом, игнорируем");
    
print("Сумма цифр в числе:",sum_rank);
с
