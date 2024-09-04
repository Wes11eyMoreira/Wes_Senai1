# Desafio 2: Crie um sistema de Cadastro de um hotel
print('Hotel Transilvânia')

#Cadastro de cliente

usuarios = []

login = input("digite seu Username: ")
idade = int(input('Digite sua idade: '))

usuario1 = {
    'nome':'Weslley Moreira',
  'idade': 21
}
usuario2 = {
    'nome': 'Eric Moreira',
    'idade': 21,
}
usuario3 = {
    'nome':'Fernando Felizardo',
    'idade': 42,
}

usuarios += usuario1, usuario2, usuario3

if login == usuarios[0]['nome'] or login == usuarios[1] ['nome'] or login == usuarios [2]['nome']: 
    print("Bem vindo:", login)
    
else:
    print("Usuario não encontrado!!! Necessario Cadastrar no sistema: ")
    novo_usuario = {
        'Digite seu nome': input('Digite seu nome: '),
        'Idade': input('Digite sua idade: ')
    }
    print('Sejá bem vindo',novo_usuario['Digite seu nome'])
    usuarios.append(novo_usuario)

print(f'''..................................................................
Quartos Disponiveis
      ''')
print(f'''
      1. Quarto simples: R$100 por dia
      2. Quarto duplo: R$150 por dia 
      3. Quarto luxo: R$250 por dia
''')

valor_quarto1 = 100
valor_quarto2 = 150
valor_quarto3 = 250

escolha1_usuario1 = int(input("Escolha o número correspondente ao primeiro quarto escolhido: "))
if escolha1_usuario1 == 1:
    print('Quarto simples: 100')
    diarias1 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario1 = valor_quarto1*diarias1 
    print('Valor total das diarias R$',valor_total_usuario1)
elif escolha1_usuario1 == 2:
    print('Quarto duplo: 150 ')
    diarias2 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario1 = valor_quarto2*diarias2
    print('Valor total das diarias R$',valor_total_usuario1)
elif escolha1_usuario1 == 3:
    print('Quarto luxo: 250 ')
    diarias3 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario1 = valor_quarto3*diarias3
    print('Valor total das diarias R$',valor_total_usuario1)

escolha2_usuario2 = int(input("Escolha o número do quarto correspondente ao segundo quarto escolhido: "))
if escolha2_usuario2 == 1:
    print('Quarto simples: 100')
    diarias1 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario2 = valor_quarto1*diarias1
    print('Valor total das diarias R$',valor_total_usuario2)
elif escolha2_usuario2 == 2:
    print('Quarto duplo: 150 ')
    diarias2 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario2 = valor_quarto2*diarias2
    print('Valor total das diarias R$',valor_total_usuario2)
elif escolha2_usuario2 == 3:
    print('Quarto luxo: 250 ')
    diarias3 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario2 = valor_quarto3*diarias3
    print('Valor total das diarias R$',valor_total_usuario2)

escolha3_usuario3 = int(input("Escolha o número do quarto correspondente ao terceiro quarto escolhido: "))
if escolha3_usuario3 == 1:
    print('Quarto simples: 100')
    diarias1 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario3 = valor_quarto1 * diarias1
    print('Valor total das diarias R$',valor_total_usuario3)
elif escolha3_usuario3 == 2:
    print('Quarto duplo: 150 ')
    diarias2 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario3 = valor_quarto2 * diarias2
    print('Valor total das diarias R$',valor_total_usuario3)
elif escolha3_usuario3 == 3:
    print('Quarto luxo: 250 ')
    diarias3 = int(input('Escolha a quantidades de Diarias: '))
    valor_total_usuario3 = valor_quarto3 * diarias3 
    print('Valor total das diarias R$',valor_total_usuario3)


print(f'''
..............................................
O valor a ser pago é de R${valor_total_usuario1+valor_total_usuario2+valor_total_usuario3}
      Pagamento a vista ou no Pix: R${10%valor_total_usuario1+valor_total_usuario2+valor_total_usuario3}<
      Pagamento parcelado em 10x{valor_total_usuario1+valor_total_usuario2+valor_total_usuario3/10:.2f}<
..............................................
''')
