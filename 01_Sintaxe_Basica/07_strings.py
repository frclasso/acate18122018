#!/usr/bin/env python3

str  ="Hello Python "

# Indexando
print(str[0]) # indexando, imprime primeiro elemento
print(str[1]) # indexando, imprime segundo elemento
print(str[-1]) # indexando, imprime ultimo elemento

# Fatiando / Slicing
print(str[2:5]) # fatiando a partir do terceiro elemento até o quinto(exclusivo)
print(str[2:])# fatiando a partir do terceiro elemento

"""Concatenação de strings"""
print(str + " 2018")

str2 = " 3, Standard Library."
print(str + str2) # concatenação de strings

str4 = (str + str2)

'''Repeticao *'''
print(str * 5)

'''Alguns métodos de string'''
print(str4.upper()) # imprime todas as letras maiusculas
print(str4.lower()) # imprime minusculas
print(str4.capitalize()) # Primeira letra maiuscula
print(str4.title()) # primeira letra de cada palavra maiuscula
print(str4.swapcase()) # inverte o case
print(str4[::-1]) # invertendo uma string


print()
str3 = """\t\tThis is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, \twhether explicitly given like
this within the brackets [ \n\n], or just a NEWLINE within
the variable assignment will also show up.
"""
#print(str3)  # com aspas triplas imprime no formato digitado

