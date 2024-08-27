my_dict = {'Ivan': 1964, 'Maria': 1980, 'Alex': 2005}
print('Словарь:', my_dict)
print('Существуещее значение:', my_dict.get('Ivan'))
print('Несуществующее значение:', my_dict.get('Artem'))
my_dict['Petr'] = 1999
my_dict['Artem'] = 1987
print('Удаленное значение:', my_dict.pop('Maria'))
print('Изменный словарь:', my_dict)
print()
my_set = {1, 'text', 1, 1.12, 'text', 1}
print('Множество:', my_set)
my_set.add('Ivan')
my_set.add(4.99)
my_set.discard(1)
print('Измененное множество:', my_set)