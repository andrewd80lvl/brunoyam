import math

def area(a,b,c):

        if(c > a+b or b > a+c  or a > b+c ):
                print("Одна сторона треугольника больше суммы двух других сторон.")
                return 0

        area_triangle = float(0) # Площадь треугольника
        
        p = (a+b+c)/2 # Полупериметр
        area_triangle = math.sqrt((p*(p-a)*(p-b)*(p-c)))

        return area_triangle


print(area(6,10,20)) # выводим ошибку

print(area(20,20,20)) # выводим площадь треугольника
