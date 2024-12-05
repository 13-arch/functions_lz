def tempr(a):
    b=(a*1.8)+32
    return(b)
temp=int(input('введите температуру в градусах Цельсия: ')) 
result1=tempr(temp)
print('температура в градусах по фаренгейту равна:',result1)