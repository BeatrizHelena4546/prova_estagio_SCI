"""
    3ª questão - Prova SCI
"""
nomes = []
notas = []
medias = []

while True:
    nome = input('Digite o nome do aluno: ')
    nomes.append(nome)
    
    for i in range(4):
        nota = float(input(f'Digite a {i+1}: '))
        notas.append(nota)
        
    
    print("Aluno", nome)
    print("Media", )
        
    
    opcao = input("Deseja encerrar? Digite 's' para sim ou 'n' para não: ")
    
    if opcao == "s":
        break
    
    


