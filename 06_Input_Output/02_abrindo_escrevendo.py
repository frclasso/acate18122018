#!/usr/bin/env python3


f = open('arquivo.txt', 'w')


print('Informacoes do arquivo')
nome_do_arquivo = f.name
modo = f.mode
print('Name: ', f.name)
print('Mode: ', f.mode)
print('Alteracoes salvas com sucesso')

f.write('Primeira linha do arquivo')
f.write('\nSegunda linha do arquivo')
f.write('\nTerceira linha do arquivo')
f.write('\nQuarta linha do arquivo')
f.write('\nQuinta linha do arquivo')
f.write('\nSexta linha do arquivo')


# fechando
f.close()
