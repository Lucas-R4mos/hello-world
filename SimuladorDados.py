from random import randint
print('Simulador de dado.')
continuar = ''
while continuar == '' or continuar == 's':
    continuar = ''
    quantidade = input('Informe a quantidade de dados: ')
    lados = input('Informe a quantidade de lados dos dados: ')
    for x in range(quantidade):
        resultado_dado = (randint(1, lados))
        print('Dado {} (d{}) = {}'.format(x + 1, lados, resultado_dado))
    while continuar != 'n' and continuar != 's':
        continuar = input('Deseja continuar? (s/n) ')