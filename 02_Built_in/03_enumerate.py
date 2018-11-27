#!/usr/bin/env python3
#
# animals = ('cat', 'dog','rabbit', 'monkey', 'bird')
# for i, v in enumerate(animals,start=1):
#     print(f'{i}:{v}')


clientes = {
    '11223344':'Fabio',
    '22112233':'Joanna',
    '33221122':'Karbony',
    '44332211':'Andre',
    '55443322':'Jonas',
    '66554433':'Cesar',
    '77665566':'Juliana'
}
print()
print(f'Foram encontrados {len(clientes)} registros')
print()
for k,v in enumerate(clientes.items(),start=1):
    print(k, v[0],v[1] )