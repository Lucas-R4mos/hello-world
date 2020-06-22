from random import randint
import time
import sys

def check_inteiro(pergunta, resposta):
    while not resposta.isnumeric():
        print('Opção inválida.')
        resposta = input(pergunta)
    return int(resposta)

def rolagem_dado(dado):
    for i in range(10):
        rolagem = randint(1, lados)
        time.sleep(0.1)
        print('\rDado {} (d{}) = {:02d}'.format(dado, lados, rolagem),end='\r')
        
perguntas_inteiro = ('Informe a quantidade de dados: ', 'Informe a quantidade de lados: ')

print('Simulador de dado.')
continuar = ''

while continuar == '' or continuar == 's':
    continuar = ''
    quantidade = input(perguntas_inteiro[0])
    quantidade = check_inteiro(perguntas_inteiro[0], quantidade)
    lados = input(perguntas_inteiro[1])
    lados = check_inteiro(perguntas_inteiro[1], lados)       

    for x in range(quantidade):
        rolagem_dado(x + 1)
        print('Dado {}'.format(x + 1))
                
    while continuar != 'n' and continuar != 's':
        continuar = input('Deseja continuar? (s/n) ')
