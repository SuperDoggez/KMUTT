c,n=[int(i) for i in input().split()]
for i in range(1,n+1):
    print(((' '*(4-len(str(i))))+('%d'%i)+(' '*(3))+'|'),end='')
    for k in range(1,c+1):print((('  ')+('%.3f'%((1+(k/100))**i))+(' ')+'|'),end='') 