print('\nCom uma trena, meça a largura e a altura das paredes e depois multiplique estas metragens.')
r = float(input('Digite o valor da metragem. Ex.:(15.6): '))
demao = input('\nHaverá demão?\n Se sim, digite quantas demãos, se não só aperte -Enter- :  ')
lt = 2

if demao == '':
    total = r / lt

if demao != '':
    total = (r*float(demao))/lt

print('A área a ser pintada é {} e sabendo que 1 litro de tinta é possível pintar 2m², então será necessário {} litros de tinta.'.format(r , total))