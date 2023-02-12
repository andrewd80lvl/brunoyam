import json

#level 1
def register(login,passwd):

    with open('shadow','r') as sh_file: # считываем словать логин:паролей
        data = json.load(sh_file)
        
    if login not in data.keys(): # level 2 проверяем уникальность регистрируемого логина
        data[login] = passwd
    else:
        print("Пользоватиль с таким именем уже зарегистрирован.")

    with open('shadow','w') as sh_file:  # Добовляем логин в файл
        json.dump(data,sh_file)
    
    return

#level 3
def function(login,passwd):

    with open('shadow','r') as sh_file: # считываем словать логин:паролей
        data = json.load(sh_file)

    if login not in data.keys(): # проверяем зарегистрирован  логин
        print("Ошибка аутентификации. Пользоватиль с таким именем не найден.")
        return False

    if passwd == data[login]:
        print("Вы зарегестрированы в системе. Ответ на основной вопрос: 42")
        return True
    else:
        print("Ошибка аутентификации. Несовпадение пароля")
        return False


quest = input("Желаете войти в систему или зарегистрироваться. Введите login или reg\n")
if(quest == "login"):
    req_data = input("Для входа в систему введите login:password\n")
    d = req_data.split(':')
    function(d[0] , d[1])

elif(quest == "reg"): # Регистрация в системе нового пользователя
    req_data = input("Для регистрации введите логин и пароль в формате login:password\n")
    d = req_data.split(':')
    register(d[0] , d[1])
else:
    print("Ошибка ввода команды")
