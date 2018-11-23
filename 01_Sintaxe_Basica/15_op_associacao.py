#!/usr/bin/env python3

# Operadores de atribuição - Members ship operators
# in e not in

# em listas
cursos = ['Historia', 'Matematica', 'Fisica','Quimica', 'Economia' ]
print('Economia' in cursos) # True
print('Historia' not in cursos) # False
print('Geografia' not in cursos) # False
print()

# em tuplas
codes = (1234, 4556, 34455, 6677)
print(4556 in codes)
print(3445 not in codes)
print()

# em strings
str = 'Python'
print('P' in str)
print('p' not in str)
print()

# em dicionarios
aluno = {'ID': 1223,'Nome':'Patricia','Idade': 27,'Curso': 'Sistemas de Informação','Turno':'Noturno'}
print('Nome' in aluno)
print('Patricia' in aluno) # False
print('Patricia' in aluno.values()) # True