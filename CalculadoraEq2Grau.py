print('--------------------------------------')
print('Calculadora de equação do segundo grau')
print('Para equações do tipo ax² + bx + c = 0')
print('informe os valores de a, b e c.')
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
if a == 0:
    print('A equação não é do segundo grau.')
    exit()
else:
    print('{}x² + {}x + {} = 0'.format(a, b, c))
d = b ** 2 - 4 * a * c
print('Delta:{}'.format(d))
rd = d ** 0.5
x1 = ((rd - b)/(a * 2))
x2 = ((-1 * rd - b)/(a * 2))
if d > 0:
    print('A equação possui duas raízes reais')
    print('e diferentes, sendo elas:')
    print('x1 = {}'.format(x1))
    print('x2 = {}'.format(x2))
elif d == 0:
    print('A equação possui uma raíz real,')
    print('sendo ela:')
    print('x = {}'.format(x1))
else:
    print('A equação não possui raízes reais.')
print('--------------------------------------')