def rad(r):#задаем функцию
    S=3.14*r**2#задаем значения функции
    return S
def dlin(r):
    C=2*3.14*r
    return C
  

chislo=int(input('введите число: ')) 
result1=rad(chislo)#вызов функции 
result2=dlin(chislo)
print('длина окружности равна:',result2)
print('площадь круга равна:',result1)#вывод функии




