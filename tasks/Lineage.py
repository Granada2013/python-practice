"""
Pythontutor
"Родословная: подсчет уровней"

В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. 
У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
Вам дано генеалогическое древо, определите высоту всех его элементов.
Программа получает на вход число элементов в генеалогическом древе N. 
Далее следует N−1 строка, задающие родителя для каждого элемента древа, кроме родоначальника. 
Каждая строка имеет вид имя_потомка имя_родителя.
Программа должна вывести список всех элементов древа в лексикографическом порядке. 
После вывода имени каждого элемента необходимо вывести его высоту.
"""


d_rod = dict()                    #создаем словарь "ребенок - родитель"
d_reb = dict()                    #создаем словарь "родитель - ребенок(дети)"
n = int(input())
for i in range(n - 1):
  rebenok, roditel = input().split()
  d_rod[rebenok] = roditel
  if roditel not in d_reb.keys():
    d_reb[roditel] = [rebenok]
  else:
    d_reb[roditel].append(rebenok)  
 
d = {}                              #создаем словарь "имя человека - номер его поколения (высота)"
for key in d_reb.keys():            #находим родоначальника, сопоставляя ключи словарей "родитель - ребенок" и "ребенок - родитель" 
  if key not in d_rod.keys():       #(человек с этим именем родитель, но не ребенок)
    d[key] = 0                      #присваиваем ему высоту 0 (поколение 0)
    break
    
for key in d_rod.keys():           #перебираем всех людей по очереди (перебирая ключи словаря "ребенок - родитель")
  if d_rod[key] in d.keys():       #если родитель человека уже в есть среди ключей словаря d:
    d[key] = d[d_rod[key]] + 1     #номер поколения этого человека на 1 больше, чем у его родителя (добавляем значения в словарь d)
  
  else:                            #иначе:   
    i = key                        #вводим переменную i, котоаря в цикле будет менять имя человека на имя его родителя
    cnt = 1                        #вводим счетчик поколений
    while d_rod[i] not in d.keys():#пока родитель не входит в ключи словаря d:
      i = d_rod[i]                 #меняем человека на его родителя
      cnt += 1                     #и увеличиваем счетчик
    d[key] = d[d_rod[i]] + cnt     #на выходе из цикла присваиваем человеку номер его поколения

l = [key for key in d.keys()]      #выводим на экран в алф порядке имя человека и номер его пколения (высоту в родословной)
l.sort()
for i in l:
  print(i, d[i])