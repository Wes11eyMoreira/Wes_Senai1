#Sistemas de notas do alunos

print("Sistemas de notas dos alunos 3B")

aluno1 = []
aluno2 = []
aluno3 = []

nome1 = str(input('Digite o nome do primeiro aluno: '))
aluno1_nota1 = float(input("Digite a sua nota de Português >> "))
aluno1_nota2 = float(input("Digite a nota de Matematica >> "))
aluno1_nota3 = float(input("Digite a sua nota de Inglês >> "))

nome2 = str(input('Digite o nome do segundo Aluno: '))
aluno2_nota1 = float(input("Digite a sua nota de Português >> "))
aluno2_nota2 = float(input("Digite a sua nota de Matematica >> "))
aluno2_nota3 = float(input("Digite a sua nota de Inglês >> "))

nome3 = str(input('Digite o nome do terceiro Aluno: '))
aluno3_nota1 = float(input("Digite a sua nota de Português >> "))
aluno3_nota2 = float(input("Digite a sua nota de Matematica >> "))
aluno3_nota3 = float(input("Digite a sua nota de Inglês >> "))

aluno1 += (aluno1_nota1,aluno1_nota2,aluno1_nota3)
aluno2 += (aluno2_nota1,aluno1_nota2,aluno1_nota3)
aluno3 += (aluno3_nota1,aluno3_nota2,aluno3_nota3)
media_geral = sum(aluno1),sum(aluno2),sum(aluno3)


print(f'''
Notas do {nome1}: {aluno1}
media do {nome1}: {sum (aluno1)/ len(aluno1):.2f}
.......................................
Notas do {nome2}: {aluno2}
Media do {nome2}: {sum(aluno2)/len(aluno2):.2f}
......................................
Notas do {nome3}: {aluno3}
Media do {nome3}: {sum(aluno3)/len(aluno3):.2f}
......................................
Média Geral: {sum(media_geral)/9:.2f}
''')