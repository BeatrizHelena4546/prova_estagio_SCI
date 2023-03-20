"""
    4ª questão - Prova SCI 
"""

vetor = [0] * 5

for i in range(5):
    n = float(input(f"Digite o {i+1}º numero: "))
    vetor[i] = n

print("Numero da posição 3 dentro do vetor: ", vetor[2])
