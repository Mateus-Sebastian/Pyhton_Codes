import os
quantidadenotas = int
soma = 0
concluido = False
while concluido == False:
    quantidadenotas = int(input('Quantas notas a serem calculadas?\n'))

    for i in range(1,quantidadenotas+1):
        nota = float(input('Digite a nota %.0f: '%i))
        soma += nota

    if quantidadenotas == 0:
        input('Valor %.0f'%quantidadenotas + ' inválido.\nTente novamente.')
        os.system('clear')
    else:
        print('\nA média das notas é %.1f'%(soma / quantidadenotas))
        concluido = True