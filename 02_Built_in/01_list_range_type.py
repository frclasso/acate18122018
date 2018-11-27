# Convertendo um tupla em lista

numTuple = (1,2,3,4,5)
numList = list(numTuple)
print(numList)

# Verificando o tipo com type
print(type(numTuple))
print(type(numList))
print()

# Start
print(range(10))
print(list(range(10)))

# Start e Stop
print(range(1, 11))
print(list(range(1, 11)))

# Start - Stop - Step
print(range(0, 30, 5))
print(list(range(0, 30, 5)))

print(range(0, 10, 3))
print(list(range(0, 10, 3)))

print(range(0, -10, -1))
print(list(range(0, -10, -1)))

print(range(0))
print(list(range(0)))

print(range(1, 0))
print(list(range(1, 0)))

# exemplo 2

# numberedContestants = range(30)
#
# print(list(numberedContestants))
#
# for c in list(numberedContestants):
#     print("Contestants: " + str(c) + " is here!")