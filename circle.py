def rad(r):
    S=3.14*r**2
    return S

def dlin(r):
    C=2*3.14*r
    return C
  

chislo=int(input('введите число: ')) 
result1=rad(chislo) 
result2=dlin(chislo)
print('длина окружности равна:',result2)
print('площадь круга равна:',result1)




