n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
r = (n1+n2)

print('A soma entre {0} e {1} é igual a {2}'.format(n1, n2, r))

s1 = str(n1)
s2 = str(n1)

print('A concatenação dos números é: ' + s1 + s2)

print('Tipo variável n1: {} cujo valor {}.'.format(type(n1), n1))
print('Tipo variável s1: {} cujo valor {}.'.format(type(s1), s1))
f1 = float(n1)
print('Conversão variável para float {} cujo valor {}.'.format(type(f1), f1))
b1 = bool(n1)
print('Conversão variável para boleano {} cujo valor {}.'.format(type(b1), b1))
print('Variável s1 contém número: {}'.format(s1.isnumeric()))
print('Variável n1 contém alpha: {}'.format(s1.isalpha()))
print('Variável n1 contém alphanumeric: {}'.format(s1.isalnum()))
