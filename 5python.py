"""
    5ª questão - Prova SCI 
"""

nomes = []
notas = []

for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nomes.append(nome)
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Digite a {j+1} nota"))
        notas.append(nota)

medias_alunos = []
for i in range(3):
    soma_notas = sum(notas[i])
    media = soma_notas / 4
    medias_alunos.append(media)
    print("Aluno: ", nomes[i]," / Media: ", media)

indice_maior_media = medias_alunos.index(max(medias_alunos))
indice_menor_media = medias_alunos.index(max(medias_alunos))

print("aluno com maior media: ", nomes[indice_maior_media])
print("aluno com menor media: ", nomes[indice_menor_media])
