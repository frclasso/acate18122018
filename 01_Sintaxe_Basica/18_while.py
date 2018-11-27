#!/usr/bin/env python3
# -*-coding:utf-8 -*-


# Incrementando
# count = 0
#
# while (count < 9):
#     print('Contador:', count)
#     count = count + 1 # incrementador
# print("Fim!")


# Decrementando

import time

# Utilizando o modulo time para criar um timer

seconds = 6
while seconds != 0:
    print(f"Voce tem apenas {seconds} segundos para respoder...")
    time.sleep(2)
    seconds -=1
print('Game Over, You Will Die!')
print('####### Buuuuuuuuuuuum! #######')