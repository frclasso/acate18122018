#!/usr/bin/env python3

cursos = ['Historia', 'Matematica', 'Fisica','Quimica', 'Economia' ]

# Indexando
# print(cursos[0])
# print(cursos[1])
# print(cursos[2])
# print(cursos[3])
# print()

# # Fatiando/ Slincing
# print(cursos[:]) # acessa lista completa
# print(cursos[0:4]) # do primeiro ao quinto(exclusivo)
# print(cursos[:3]) # do primeiro ao terceiro(exclusivo)
# print(cursos[2:]) # a partir do terceiro elemento
# print()


'''Adicionando  novos items a lista'''
# cursos.append('Artes')  # adiciona ao final da lista
# cursos.insert(0, 'Biologia') # adiciona na posição do indice especifidao
# print(cursos)
# print()

'''Adicionado novos  items de outra lista'''
# cursos_2 = ['Fotografia', 'Musica']
#
# cursos.extend(cursos_2)
# print(cursos)
# print()

'''Removendo items de uma lista'''

# Utilizando o método remove
# cursos.remove('Matematica')
# print(cursos)
# print()

# Utilizando o método pop
# cursos.pop()  # Caso nao seja passado nenhum parametro elimina o ultimo item
# cursos.pop(1) # passando um indice como parametro
# print(cursos)
# print()
#
# Utiliazndo o método del
# del cursos[0] # deleta via indice o primeiro elemento
# print(cursos)
# print()

# Ordenando Listas
numeros = [1,2,3,5,11,10,12,0,7,6,9,8,4]

# numeros.sort()
# numeros.reverse()
# print(numeros)

#numeros.sort(reverse=True)
#print(numeros)
#print()

# copiando elementos de uma lista
# cursos3 = cursos
# print(cursos)
# print(cursos3)
# print()
# print(f'Identificador de cursos  {id(cursos)}')
# print(f'Identificador de cursos3 {id(cursos3)}')
# print()
# cursos3[0] = 'Letras'
# print(cursos3)
# print(cursos)
# print()
#
# cursos4 = cursos[:]
# print(cursos4)
# print(cursos)
# print()
# print(f'Identificador de cursos4 {id(cursos4)}')
# print(f'Identificador de cursos {id(cursos)}')
# print()
# cursos4[0] = 'Finanças'
# print(cursos4)
# print(cursos)
# print()

'''criando uma lista vazia'''
# listaVazia = []
# print(listaVazia)
# print(type(listaVazia))

'''Deletando a lista'''
# del cursos4
# print(cursos4)
