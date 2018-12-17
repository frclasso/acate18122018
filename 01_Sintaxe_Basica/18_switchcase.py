#!/usr/bin/env python3


# simulando switch case em Python

menu = int(input("""Escolha um opção:
Digite 1 para cadatro de novos clientes
Digite 2 para listas clientes
Digite 3 para alterar registro existente
Digite 4 para apagar registro
Digite 0 para sair: """))
print()

while True:
    if menu == 0:
        print('Saindo...')
        break
    elif menu == 1:
        print('Voce escolheu Cadastro de Novos clientes')
        break
    elif menu == 2:
        print('Voce esolheu Listar clientes cadastrados')
        break
    elif menu == 3:
        print('Voce escolheu Alterar um regitro existente')
        break
    elif menu == 4:
        print('Voce escolheu Apagar um registro')
        break
