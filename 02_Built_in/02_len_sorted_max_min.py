#!/usr/bin/env python3

# len, sorted,min, max


clientes = {
    '65223344':['Classo', 'Fabio', 44,'M','045045045',99998888,'MasterCard', 12345-0, '10/19', 215],
    '22112233':['Ferreira', 'Joanna', 28,'F','345665045',99998888,'VISA', 12345-0, '10/19', 215],
    '43221122':['Pereira ', 'Karbony', 39,'M','045045045',99998888,'Nubank', 12345-0, '10/19', 215],
    '84332211':['Faccin ', 'Andre', 37,'M','045045045',99998888,'PayPal', 12345-0, '10/19', 215],
    '15443322':['Cardoso', 'Jonas', 46,'M','045045045',99998888,'Credicard', 12345-0, '10/19', 215],
    '66554433':['Lopes', 'César', 42,'M','045045045',99998888,'Elo', 12345-0, '10/19', 215],
    '27665566':['Reis ', 'Juliana', 40,'F','045045045',99998888,'American Express', 12345-0, '10/19', 215],
    '78665577':['Neto', 'Ramiro', 74,'M','045045045',99998888,'Dinners Club', 12345-0, '10/19', 215]
}
print(f'Nosso cadastro conta com: {len(clientes)} clientes.')
print()

# print('Do mais recente para o mais antigo:')
# for k,v in sorted(clientes.items(),reverse=True): # reverse=True, do maior pro menor
#     print(k, v)
# print()
#
#
# # Por ordem alfabética [1] = lista , [1] = segundo item da lista, nome
# print('Ordenando por ordem alfabética:')
# for k,v in sorted(clientes.items(), key=lambda clientes:clientes[1][1]):
#     print(k, v)
# print()
#
#
# print('Ordenando pela idade:')
# for k,v in sorted(clientes.items(), key=lambda clientes:clientes[1][2]):
#     print(k, v)
# print()
#
#
print(f'Cadastro mais recente, ID: {max(clientes)}')
print(f'Cadastro mais antigo,  ID: {min(clientes)}')
print()
