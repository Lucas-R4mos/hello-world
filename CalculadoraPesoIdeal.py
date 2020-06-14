print('Descubra seu peso ideal.')
h = float(input('Informe a sua altura em metros:'))
ph = round(((h * 72.7) - 58),2)
pm = round(((h * 62.1) - 44.7),2)
c = {0}
while len(c) < 2:
    s = input('Informe seu sexo: h ou m?')
    if s == 'h':   
        print('Seu peso ideal é {} Kg.'.format(ph))
        c.add(1)
    elif s == 'm':
        print('Seu peso ideal é {} Kg.'.format(pm))
        c.add(1)
    else:
        0

pa = float(input('Qual seu peso atual?'))
absh = round((abs(pa - ph)),2)
absm = round((abs(pa - pm)),2)
if s =='h':
    if pa > ph:
        print('Você precisa perder {} Kg'.format(absh))
    else:
        print('Você precisa ganhar {} Kg'.format(absh))
else:
    if pa > pm:
        print('Você precisa perder {} Kg'.format(absm))
    else:
        print('Você precisa ganhar {} Kg'.format(absm))