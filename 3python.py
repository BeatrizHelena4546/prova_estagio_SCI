"""
    3ª questão - Prova SCI
"""
nomes = []
notas = []

while True:
    nome = input('Digite o nome do aluno: ')
    nomes.append(nome)
    notas_alunos = []
    for i in range(4):
        nota = float(input(f'Digite a {i+1}ª nota: '))
        notas_alunos.append(nota)
    notas.append(notas_alunos)
        
    medias_aluno = []
    for i in range(len(nomes)):
        soma_notas = sum(notas[i])
        media = soma_notas / 4
        medias_aluno.append(media)
        if media < 6:
            AouR = "Reprovado"
        else:
            AouR = "Aprovado"
    print("Aluno: ", nomes[i], " / Media: ", media, " / Situação: ", AouR)    
        
    opcao = input("Deseja encerrar? Digite 's' para sim ou 'n' para não: ")
    
    
    if opcao == "s":
        break
    
    


