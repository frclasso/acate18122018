# Lendo uma linha

# usando o with nao precisa fazer o close()
# with open('arquivo.txt', 'r') as f:
#     for l in f.readline():
#         print(l,end='')

# lendo mais de uma linha

with open('arquivo.txt', 'r') as f:
    for l in f.readlines(77): # 25 primeira linha, 26 segunda, 51 terceira, 77 quarta
        print(l,end='')

