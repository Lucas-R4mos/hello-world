print('----------------------------------------------')
print('Informe um número inteiro menor que 1000 e te')
print('direi quantas centenas, dezenas e unidades')
print('ele possui.')
n = int(input('Número: '))
if n <= 0 or n >= 1000:
    print('Insira um número válido.')
    exit()
else:
    n = n
c = ()
d = ()
u = ()
print('----------------------------------------------')
if n / 100 < 1:
    c = 0
else:
    c = round(((n / 100) - ((n % 100) / 100)),0)

nd = n - 100 * c
if nd / 10 < 1:
    d = 0
else:
    d = round(((nd / 10) - ((nd % 10) / 10)),0)

u = round((nd - d * 10),0)

pc = ()
if c == 1:
    pc = ('{} centena'.format(u))
elif c > 1:
    pc = ('{} centenas'.format(c))
else:
    pc = ()

pd = ()
if d == 1:
    pd = ('{} dezena'.format(d))
elif d > 1:
    pd = ('{} dezenas'.format(d))
else:
    pd = ()

pu = ()
if u == 1:
    pu = ('{} unidade'.format(u))
elif u > 1:
    pu = ('{} unidades'.format(u))
else:
    pu = ()

if c != 0 and d != 0 and u != 0:
    print('{} = {}, {} e {}'.format(n, pc, pd, pu))
elif c != 0 and d != 0 and u == 0:
    print('{} = {} e {}'.format(n, pc, pd))
elif c != 0 and d == 0 and u != 0:
    print('{} = {} e {}'.format(n, pc, pu))
elif c != 0 and d == 0 and u == 0:
    print('{} = {}'.format(n, pc))
elif c == 0 and d != 0 and u != 0:
    print('{} = {} e {}'.format(n, pd, pu))
elif c == 0 and d != 0 and u == 0:
    print('{} = {}'.format(n, pd))
elif c == 0 and d == 0 and u != 0:
    print('{} = {}'.format(n, pu))
else:
    print('EOQ?')

print('----------------------------------------------')