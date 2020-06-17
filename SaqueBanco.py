print('------------- Caixa eletrônico -------------')
print('Saque mínimo: R$ 10,00')
print('Saque máximo: R$ 600,00')
print('--------------------------------------------')
print('INFO: Disponíveis apenas notas de R$ 100,00,')
print('INFO: R$ 50,00, R$ 10,00, R$ 5,00 e R$ 1,00.')
print('--------------------------------------------')
ok = 1
while ok == 1:
    saq = int(input(('Informe o valor do saque: ')))
    if saq > 600:
        print('R$ {},00: Valor ultrapassa o saque máximo.'.format   (saq))
        ok = ok
    elif saq < 10:
        print('R$ {},00: Valor menor que o saque mínimo.'.format    (saq))
        ok = ok
    else:
        print('R$ {},00: verifique a quantidade de cédulas:'.   format(saq))
        ok = ok + 1

n100 = ((saq - (saq % 100))/ 100)
if n100 > 0:
    print('{} nota(s) de R$ 100,00'.format(n100))
else:
    0
res = saq - (100 * n100)
n50 = ((res - (res % 50))/ 50)
if n50 > 0:
    print('{} nota(s) de R$ 50,00'.format(n50))
else:
    0
res = res - (50 * n50)
n10 = ((res - (res % 10))/ 10)
if n10 > 0:
    print('{} nota(s) de R$ 10,00'.format(n10))
else:
    0
res = res - (10 * n10)
n5 = ((res - (res % 5))/ 5)
if n5 > 0:
    print('{} nota(s) de R$ 5,00'.format(n5))
else:
    0
res = res - (5 * n5)
n1 = res
if n1 > 0:
    print('{} nota(s) de R$ 1,00'.format(n1))
else:
    0

ok = 1
while ok == 1:
    conf = input('Confirmar saque? "s"im ou "n"ão? ')
    if conf == 's':
        print('Retire o dinheiro')
        print('.')
        print('.')
        print('.')
        print('Obrigado!')
        ok = ok + 1
    elif conf == 'n':
        print('Saque cancelado.')
        ok = ok + 1
    else:
        ok = ok
        print('Opção inválida.')
print('--------------------------------------------')
