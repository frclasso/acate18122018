#!/usr/bin/env python3

code = 'Python'
versao = 3.7
ano = 2018


# place holder
""""% python 2.7, "%"
 place holder %s (strings) , %d(inteiros) %f(floats)
 """

print('Em %d, vamos programar em %s versão %.1f.' % (ano, code, versao))

# # formato Python versao 3.0
print('Em {}, vamos programar em {} versao {:.1f}.'.format(ano,code, versao))

# # versao 3.5.6
# # f'{}'
print(f'Em {ano}, vamos programar em {code} versao {versao}')