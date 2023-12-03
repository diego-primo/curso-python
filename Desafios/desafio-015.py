dias = float(input('Quantos dias alugados? '))

kms = float(input('Quantos KMs rodados? '))

pagoPorDia = dias * 60
pagoPorKM = kms * 0.15


print('O Total a pagar é de R$:{:.2F}'.format(pagoPorDia + pagoPorKM))
