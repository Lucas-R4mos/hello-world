print('Investigação criminal')
perguntas = ['Telefonou para a vítima? (s/n): ', 
'Esteve no local do crime? (s/n): ', 
'Mora perto da vítima? (s/n): ', 
'Devia para a vítima? (s/n): ', 
'Já trabalhou com a vítima? (s/n): ']
culpa = []
for pergunta in perguntas:
    resposta = []
    while resposta != 's' and resposta != 'n':
        resposta = input(pergunta)
        if resposta == 's':
            culpa.append(pergunta)
        if resposta != 's' and resposta != 'n':
            print('Opção Inválida.')
if len(culpa) == 5:
    print('Assassino!')
elif len(culpa) == 3 or len(culpa) == 4:
    print('Cúmplice.')
elif len(culpa) == 2:
    print('Suspeito...')
else:
    print('Sabe de nada, inocente...')