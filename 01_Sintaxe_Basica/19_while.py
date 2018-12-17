#!/usr/bin/env python3
# -*-coding:utf-8 -*-


# Incrementando
count = 0

# while (count < 9):
#     print('Contador:', count)
#     count = count + 1 # incrementador
# print("Fim!")


# Decrementando
# # Utilizando o modulo time para criar um timer

import time

seconds = 4
while seconds != 0:
    print(f"Voce tem apenas {seconds} segundos para respoder...")
    time.sleep(2)
    seconds -=1
print('Game Over, You Will Die!')
print('####### Buuuuuuuuuuuum! #######')