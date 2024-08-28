#Exercicios aula5

#1 Imprima uma mensagem de boas-vindas na tela.
print('Bem vindo')

#2  Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
num1 = bool(True)
tipo = type(num1)
print(tipo)

#3 Imprima o resultado da multiplicação de dois números decimais de sua escolha
num2 = float(35.20)
num3 = float(2.3)
resultado1 = num2 * num3
print(resultado1)

#4 Imprima o resultado da divisão de dois números inteiros de sua escolha
num4 = int(50)
num5 = int(5)
resultado2 = num4 / num5
print(resultado2)

#5 Imprima o resultado da subtração de dois números inteiros de sua escolha
num6 = int(48)
num7 = int(3)
resultado3 = num6 - num7
print(resultado3)

#6 Imprima o resultado da divisão inteira de dois números inteiros de sua escolha
num8 = int(55)
num9 = int(7)
resultado4 = int(num8 / num9)
print(resultado4)

#7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha
num10 = float(5.3)
num11 = float(2.22)
num12 = float(3.45)
num13 = float(7.1)
resultado5 = (num10 * num11 * num12 * num13 )
formato = "{:,.3f}".format(resultado5)
print(formato)

#8 Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número
num14 = 11
dobro = num14 * 2
print(dobro)

#9 Crie uma calculadora de soma com as ferramentas que vc já conhece(Use apenas input, print e variavel)
num15 = int(input('Digite um número: '))
num16 = int(input('Digite o segundo número: '))
resultado6 = (num15 + num16)
print(resultado6)

#10 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)
nomeusuario = str(input('Digite seu nome: '))
senhausuario = int(input('Digite sua senha: '))
print('sejá bem vindo', nomeusuario)















"""
lista_nomes = []
lista_notas = []
nome1 = input('Digite seu nome: ')
nota1 = float(input('Digite sua nota: '))
nome2 = input('Digite seu nome: ')
nota2 = float(input('Digite sua nota: '))
nome3 = input(' Digite seu nome: ')
nota3 = float(input('Digite sua nota: '))
lista_nomes += (nome1, nome2, nome3)
lista_notas += (nota1, nota2, nota3)

print(lista_nomes)
print(lista_nomes)



lista6 = [2,3,7,4,8,6,9,10]
organizar = sorted(lista6, reverse = True) 
print(organizar)


lista5 = [25,3,10,35,100]
menor = min(lista5)
maior = max(lista5)
print(menor, maior)


lista4 = [1,2,3]
soma = sum(lista4)
print(soma)


texto = 'python'
transforma = list(texto)
print(transforma)


lista = list(range(1,21))
print(lista)


lista1 = [10,20,30,40,50] #homogenia
print(lista1[0], lista1[1])

lista2 = ['a', 35, 3.5, 'b', 2] #heterogenia
print(lista2[3]) 

lista3 = [[10,20], [30,40], [50,60]]
print(lista3[1][0])
"""
