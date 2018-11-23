#!/usr/bin/env python3


# Sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Chemistry'}
art_courses = {'History', 'Design', 'Art', 'Math'}


'''Interseção (tem em ambos)'''
print(cs_courses.intersection(art_courses))  # Math, History

'''Diferença, o que tem em cs_courses e nao tem art_courses'''
print(cs_courses.difference(art_courses)) # CompSci,Physics,Chemistry

'''União'''
print(cs_courses.union(art_courses))
print()

"""Ou ainda poderiamos usar os seguintes operadores"""
print(cs_courses & art_courses)  # intersection
print(cs_courses - art_courses) # diference
print(cs_courses | art_courses) # union
print()


'''Filtrando duplicatas'''
print(set([1,2,1,3,1,3,2]))

'''Criando um set vazio'''
# colecao = set()  # com parenteses
# print(colecao)
# print(type(colecao))