#!/usr/bin/python3

# Itereando sobre uma string
# for letra in 'Python':
#     print(letra)

# Iterando sobre um tupla
# animals = ('bear', 'bunny', 'dog', 'cat', 'rabbit', 'duck')
#
# for pet in animals:
#     print(pet)

# Iterando sobre uma lista
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print("Current fruit is: ",index, fruits[index])


# Iterando sobre um dicionario
hospedes = {'Classo':['Fabio', 44, 'fabio@email.com', 99998888],
            'Reis':['Juliana', 40, 'juliana@email.com', 88889999],
            'Neto':['Ramiro', 74, 'ramiro@email.com', 99997777]}

for nome, dados in hospedes.items():
    print(f'Sobrenome:{nome}, Nome: {dados[0]}, Idade:{dados[1]}, email:{dados[2]}, telefone:{dados[3]}')