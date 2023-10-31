t = int(input('Vamos imprimir uma tabuada. Digite o valor: '))
print('=' * 15)
for i in range(11):
       print('{:2} x {} = {}'.format(i , t , (i*t)))
print('=' * 15)