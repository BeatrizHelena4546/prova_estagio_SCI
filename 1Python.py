"""
    1º questão - Prova SCI 
"""
ns = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º numero: "))
    ns.append(n)

pares = []
impares = []

for n in ns:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

media = sum(ns) / len(ns)

print("numeros pares: ", pares)
print("numeros impares: ", impares)
print("Media dos numeros: ", media)