my_dict={'Alex':1988, 'Katrin':1989}                     #Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
print(my_dict)                                           #Выведите на экран словарь my_dict.
print(my_dict['Alex'])                                   #Выведите на экран одно значение по существующему ключу
print(my_dict.get('Elena'))                              #Выведите на экран одно значение по отсутствующему из словаря my_dict без ошибки.
print(my_dict)                                           #Выведите на экран словарь.

my_dict.update({'Dmitri': 2014, 'Denis': 2018})          #Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#my_dict.pop('Denis')
#print(my_dict)
a=my_dict.pop('Denis')                                   #Удалите одну из пар в словаре по уществующему ключу из словаря my_dict и выведите значение из этой пары на экран.
print(my_dict)
print(a)

my_set={1,2,2,3,3,4,4,5, 'string', True, (1,2,3)}        #Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
print(my_set)                                            #Выведите на экран множество my_set (должны отобразиться только уникальные значения)
my_set.update((9,8,7), {'Sasha'}, {'bring'})         #Добавьте 2 произвольных элемента в множество my_set, которых ещё нет
print(my_set)
print(my_set.remove(1))                                  #Удалите один любой элемент из множества my_set.
print(my_set)                                            #Выведите на экран измененное множество my_set.