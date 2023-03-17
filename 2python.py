"""
    2ª questão - Prova SCI
"""
ns = []

for i in range(5):
    n = int(input(f"Digite o {i+1}: "))
    ns.append(n)

maior = max(ns)
menor = min(ns)

print("Maior numero", maior)
print("Menor numero", menor)