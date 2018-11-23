#!/usr/bin/env python3

aluno = {'ID': 1223,
         'Nome':'Patricia',
         'Idade': 27,
         'Curso': 'Sistemas de Informação',
         'Turno':'Noturno'
         }

# print(f"ID: {aluno['ID']}")
# print(f"Nome: {aluno['Nome']}")
# print(f"Idade:{aluno['Idade']}")
# print()

'''Atualizando valores existentes'''
# aluno['Idade'] = 28
# print(aluno)
# print()

'''Inserindo novo campo'''
# aluno['Matrícula'] = 8990020198
# print(aluno)
# print()

# Utilizando o metodo Update
# aluno.update({'Turno':'Diurno', 'Sobreome':'Nunes', 'Telefone':'(48)555-333'})
# print(aluno)
# print()

'''Deletando items'''
# aluno.__delitem__('Idade')
# print(aluno)
# print()

# aluno.pop('Turno')
# print(aluno)
# print()

# del aluno['Matrícula']
# print(aluno)
# print()

'''Apagando todos os dados'''
# aluno.clear()
# print(aluno)  # {}

'''Deletando o dicionario em si'''
# del aluno
# print(aluno) # NameError: name 'aluno' is not defined

'''Criando um dicionario vazio'''
# meuDic = {}
# print(meuDic)
# print(type(meuDic))
#

# print(f'Tamanho do dicionario: {len(aluno)} items.')

'''Imprimindo um dicionario com as chaves - keys()'''
# print(aluno.keys())

'''Imprimindo um dicionario com os valores - values()'''
# print(aluno.values())

'''Imprimindo um dicionario com todos os items'''
# print(aluno.items())
