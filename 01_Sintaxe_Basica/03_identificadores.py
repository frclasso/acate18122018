#!/usr/bin/env python3

'''Nao pode começar por numeros'''

#1variable = 1
#print(1variable) # SyntaxError: invalid syntax

variable1 = 'Nome ok'
print(variable1)
print()

'''Nao pode conter por simbolos'''

# !$variable1 = 'Bad Name'
# print(!$variable1) # SyntaxError: invalid syntax

# var$ = 'Bad name' # SyntaxError: invalid syntax
# print(var$)
print()

'''Case sensitive,sensível a maiuscula e minuscula'''
ManPower = 'Man'
manpower = 'man'
print(ManPower, id(ManPower))
print(manpower, id(manpower))
print()

'''Alguns exemplos de identificadores válidos'''
myClass = 'nome de uma Classe'
var_1 = 'Nome de uma variável'
Print_this_to_scren = 'Nome de uma variavel ou função'
print(myClass)
print(var_1)
print(Print_this_to_scren)
print()

# camel case
camelCaseExemplo = 'Exemplo em Camel Case'
print(camelCaseExemplo)