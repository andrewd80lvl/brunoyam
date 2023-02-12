import random
from random import randint

class Warrior:

    def __init__(self,name,health,armor,endurance,number_of_wins=0):
        self.__name = name          # Имя воина
        self.__health = health      # Здоровье
        self.__armor = armor        # Броня
        self.__endurance = endurance # Выносливость
        self.__number_of_wins = number_of_wins #Количество побед воина

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_endurance(self):
        return self.__endurance

    def reduce_endurance(self,endurance_delta): # Теряем выносливость
        self.__endurance = self.__endurance - endurance_delta

    def reduce_health(self,min,max):
        if self.__armor <= 0: # Если закончилась броня - увеличиваем урон random(10,30)
            min = 10
            max = 30

        self.__health = self.__health - random.randint(min,max)

    def action(self,type_action_self,type_action_opponent,endurance_opponent):

        if type_action_self == "attack":
            self.reduce_endurance(10)  # Наш воин атакует - теряет 10 очков выносливости

        if type_action_self == "attack" and type_action_opponent == "attack":
            if endurance_opponent <=0:
                self.reduce_health(0, 10)  # У противника закончилась выносливость - теряем здоровья от 0 до 10 единиц
            else:
                self.reduce_health(10,30) # Оба воина атакуют - теряем здоровья от 10 до 30 единиц

        if type_action_self == "protect" and type_action_opponent == "attack":
            if endurance_opponent <=0:
                self.reduce_health(0, 10)  # У противника закончилась выносливость - теряем здоровья от 0 до 10 единиц
            else:
                self.reduce_health(0,20) #  Противник атакует, наш воин защищается - теряем здоровья random(0,20)

    @staticmethod
    def select_aсtion():
        rnd = randint(0, 1)  # случайное число из [0,1]
        if (rnd == 1):  # атакуем
            return "attack"
        else:
            return "protect"


wr1 = Warrior("MadMax",100,100,100)
wr2 = Warrior("IronMan",100,100,100)

step=0
while True:

    type_action_wr1 = wr1.select_aсtion()
    type_action_wr2 = wr2.select_aсtion()

    wr1.action(type_action_wr1,type_action_wr2,wr2.get_endurance())
    wr2.action(type_action_wr2,type_action_wr1,wr1.get_endurance())

    print("Шаг:", step, " Игрок 1:", type_action_wr1," Игрок 2:", type_action_wr2 )
    print("Шаг:",step," Игрок 1:", wr1.get_name(), "(", wr1.get_health(), ")")
    print("Шаг:", step, " Игрок 2:", wr2.get_name(), "(", wr2.get_health(), ")")
    print("\n")

    # Вывод результата битвы ----------------------------------------------------
    if wr1.get_health() <= 10 and wr2.get_health() > 10:
        if wr1.get_health() <= 0:
            print("ВОИН:", wr1.get_name(), '(', wr1.get_health(), ')', "ПОГИБ!")
        else:
            print("ВОИН:", wr1.get_name(), '(', wr1.get_health(), ')', "ПОБЕЖДЕН!")

        exit(1)

    if wr2.get_health() <= 10 and wr1.get_health() > 10:
        if wr2.get_health() <= 0:
            print("ВОИН:", wr2.get_name(), '(', wr2.get_health(), ')', "ПОГИБ!")
        else:
            print("ВОИН:", wr2.get_name(), '(', wr2.get_health(), ')', "ПОБЕЖДЕН!")

        exit(2)

    if wr1.get_health() <= 10 and wr2.get_health() <= 10:
        if wr1.get_health() <= 0:
            print("ВОИН:", wr1.get_name(), '(', wr1.get_health(), ')', "ПОГИБ!")
        else:
            print("ВОИН:", wr1.get_name(), '(', wr1.get_health(), ')', "ПОБЕЖДЕН!")

        if wr2.get_health() <= 0:
            print("ВОИН:", wr2.get_name(), '(', wr2.get_health(), ')', "ПОГИБ!")
        else:
            print("ВОИН:", wr2.get_name(), '(', wr2.get_health(), ')', "ПОБЕЖДЕН!")

        exit(3)
    #------------------------------------------------------------------------------------

    step += 1






