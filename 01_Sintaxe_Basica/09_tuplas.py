"""Tuplas sao imutaveis, sendo as vezes chamadas de lisas somente leitura
   Permitem algumas operações semelhantes as de listas"""


# Definindo tuplas
minhaTupla = ('abcd', 786, 2.23, 'John', 70.2, 'this is a string')
tinyTupla = (123, 'Mary')

#print(type(minhaTupla))
#print(tinyTupla)

# Indexando

# print(minhaTupla[0])
# print(minhaTupla[1])
# print(minhaTupla[-1])
# print()

# Fatiando / Slicing

# print(minhaTupla[2:])
# print(minhaTupla[:5])
# print(minhaTupla[2:5])
# print(minhaTupla[:])
# print()

# # Concatenando tuplas
# outraTupla = minhaTupla + tinyTupla
# print(f'Concatenando: {outraTupla}')
# print()

# repetindo
# print(tinyTupla * 3)
# print()

'''Criando uma tupla vazia'''
# tuplaVazia = ()
# print(tuplaVazia)
# print(type(tuplaVazia))
# print()

'''Criando tupla com um unico elemento'''
# tuplaUmElemento = 1,  # Os parenteses são opcionais, a vírgula é obrigatória
# print(tuplaUmElemento)
# print(type(tuplaUmElemento))
# print()

# # Listas são mutáveis
# list1 = ['Historia', 'Matematica', 'Fisica','Quimica','Informática']
# list1[0] = 'Economia'
# print(list1)
# print()

## Tuplas são imutáveis
tuple_1 = ('Historia', 'Matematica', 'Fisica','Quimica','Informática')
# tuple_1[0] = 'Economia'
# print(tuple_1) # TypeError: 'tuple' object does not support item assignment
# print()

# No entanto, uma lista pode ser alterada dentro de uma tupla
# cursos = ('Historia', 'Matematica', 'Fisica','Quimica',
#           'Informática',['Artes, Musica'])
#
# print(cursos[5]) # ['Artes', 'Musica' ]
# cursos[5].append('Cênicas')
# print(cursos)

