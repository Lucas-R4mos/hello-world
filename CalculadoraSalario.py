print('------------------------------')
print('Calculadora de salário líquido')
print('------------------------------')
print('Por favor, informe o valor da')
print('hora de trabalho e a quantidade')
print('de horas trabalhadas no mês.')
valorhora = float(input('Valor por hora:'))
quantidadehora = int(input('Horas trabalhadas no mês:'))
print('------------------------------')
sbruto = round((valorhora * quantidadehora),2)
print('+ Salário Bruto = R$ {}'.format(sbruto))
ir = round((sbruto * 0.11),2)
print('- IR (11%) = R$ {}'.format(ir))
inss = round((sbruto * 0.08),2)
print('- INSS (8%) = R$ {}'.format(inss))
sindicato = round((sbruto * 0.05),2)
print('- Sindicato (5%) = R$ {}'.format(sindicato))
sliquido = round((sbruto - ir - inss - sindicato),2)
print('= Salário Líquido = R$ {}'.format(sliquido))
print('------------------------------')