'''
Продажи (pythontutor)

Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара.
Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров. 
Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.
'''

# создание словаря 
d_name = dict()
for i in range(int(input()):
  name, prod, numb = input().split()
  d_prod = dict()
  d_prod[prod] = int(numb)
  if name not in d_name.keys():
    d_name[name] = d_prod
  else:
    if prod not in d_name[name].keys():
      d_name[name].update(d_prod)
    else:
      d_name[name][prod] += int(numb)
      
# вывод словаря в требуемом формате
d = {}
for key in d_name.keys():
  l = [[key, value] for key, value in d_name[key].items()]
  l.sort()
  d[key] = l
l_2 = [key for key in d.keys()]
l_2.sort()
for i in l_2:
  print(i + ':')
  for j in d[i]:
    print(j[0], j[1])
