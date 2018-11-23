#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Comaparam o locais de memoria de dois objetos
# is e is not

num = [1, 2, 3, 4, 5 ]
num2 = num

print(num2 is num)
print(id(num))
print(id(num2))
print()

# redeclarando
num2 = [1, 2, 3, 4, 5 ]
print(num2 is num)
print(id(num))
print(id(num2))
print()

# copiando os elementos da lista num para num2
num2 = num[:]
print(num2 is num)
print(id(num))
print(id(num2))
print(num2 is not num)



