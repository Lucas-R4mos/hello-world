fruits = ('Maçã', 'Banana', 'Cereja')
print('Frutas: {}'.format(fruits))
fruteiro = []
for x in fruits:
    gosta = ''
    while gosta != 's' and gosta != 'n':
        gosta = str(input('Você gosta de {}? '.format(x)))
        if gosta == 's':
            fruteiro.append(x)
if len(fruteiro) == len(fruits):
    print('Você gosta de todas essas frutas.')
elif len(fruteiro) == 0:
    print('Você gosta de nenhuma dessas frutas.')
else:
    print('Você gosta de {} dessas frutas.'.format(len(fruteiro)))
print('Frutas que você gosta: {}'.format(fruteiro))