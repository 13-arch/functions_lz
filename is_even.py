def chetnost(a):
    if a%2==0:
        print('число',a,'четное')
    else:
        print('число',a,'нечетное')
n=int(input('введите число чтобы определить его четность: '))
result=chetnost(n)