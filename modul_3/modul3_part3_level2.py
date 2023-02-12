import math

song = ''' Было просто пасмурно, дуло с севера,
    А к обеду насчитал сто градаций серого.
    Так всегда первого ноль девятого,
    То ли весь мир сошёл с ума, то ли я — того.
    На столе записка от неё смятая,
    Недопитый виски допиваю с матами.
    Посмотрю в окно, допишу главу,
    Первое сентября, дворник жжёт листву.
    И серым облакам наплевать на нас,
    Если знаешь, как жить — живи
    Ты хотела плыть, как все — так плыви!'''


def short_words(text):

    list_text_parse = text.split()
    list_short_words = list('')

    for i in list_text_parse:
        if(len(i) < 5 and i != '—'):
            list_short_words.append(i)

    return list_short_words

print(short_words(song))

            

