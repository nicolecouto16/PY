# comando = 'start'



# if comando == 'start':
#     print('iniciar')
# elif comando == 'stop':
#     print('parar')
# else:
#     print('erro')
    
# ###############################################

# match comando:
#     case "start":
#         print('inicar')
#     case 'stop':
#         print('parar')
#     case _:
#         print('erro')
        
# ###############################################

# opcao = input("insira 1 ou 2: ")

# match opcao:
#     case '1':
#         print('cadastrar')
#     case '2':
#         print('listar')
#     case _:
#            print("valor invalido")
           
# ###############################################

# dados = ['produto', 'arroz', 10]

# match dados:
#     case ('produto', nome, qtd): #se der match ele iria aparecer o nome e a aqt
#         print(f"{nome} - {qtd}")
#     case _:
#         print("formato invalido")
           
# ###############################################   

# match lista:
#     case [1, 2, 3]:
#         print("lista completa")
#     case _:
#         print("lista incompleta")

# ###############################################

# if tipo == 'A' and status = 'ativo':
#     print("faça alguma coisa")
# elif tipo == '8' and status = 'inativo'
#     print("faça alguma coisa")

# match (lista, status):
#     case ("A", "ativo"):
#         print("faça alguma coisa")
#     case ("8", "inativo"):
#         print("faça alguma coisa")

# ###############################################
# numero = int(input("insira um numero: "))

# match numero:
#     case _ if numero %2 == 0:
#         print("par")
#     case _:
#         print("impar")
# ###############################################
        
# Ex.1 peça para o usuario numeros entre 1 e 7 mostre o dia correspondente

# opcao = input("insira uma numero de 1 a 7: ")

# match opcao:
#     case '1':
#         print('segunda')
#     case '2':
#         print('terça')
#     case '3':
#         print('quarta')
#     case '4':
#         print('quarta')
#     case '5':
#         print('quinta')
#     case '6':
#         print('sexta')
#     case '7':
#         print('sabado')
#     case _:
#         print("invalido")
           
# Ex.2 crie um sistema de menu simples, onde univrsisdade = fiap - print bem
# vindo a eng de software
 
# universidade = usp - print voce ta ferrado vai precisar estudar muito

# universidade = ITA - print voce é um monstro

# qualquer outra univrsidade, ok

# opcao = input("insira sua universidade ")

# match universidade:
#     case "fiap":
#         print('bem vindo a eng de software')
#     case 'usp':
#         print(' voce ta ferrado vai precisar estudar muito')
#     case 'ITA':
#         print('voce é um monstro')
#     case _:
#         print('ok')
        





# Ex.3 crie uma estrutura de entrata para o usuario inserir nota, caso seja maior
# ou igual a 7, print aprovado, caso seja >=5 recuperação, caso contrario, reprovado

# Ex.4 crie um algoritmo com mach/case e while paa o usuario inserir um 
# comando, digite sair para encerar

# em caso, sair, print encerrando. caso contrario, comando invalido

        


############################ FUNÇÃO ####################################

def media(a, b):
    medial = (a + b) / 2
    return medial

#utilizando/aplicando a função

print(media(10, 15))
print(media(float(input(), float(input()))))

########################################################################

def calculando(x, y):
    
    soma = x + y
    sub = x - y
    div = x / y
    mult = x * y
    
    return soma, sub, div, mult

print(calculando(100, 5))

########################Exercícios sobre função def#########################################



# 1. Crie uma função para transformar temperatura Farh em Celsius.

# 2. Crie uma função para calcular a media de 4 notas para 3 alunos.
def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


for i in range(3):
    print(f"Aluno {i+1}")

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))
    nota4 = float(input("Digite a 4ª nota: "))

    resultado = media(nota1, nota2, nota3, nota4)

    print("Média:", resultado)
    print()
# 3. Crie uma função para solicitar 5 valores para o usuário e ao final calcule a media destes valores.

# 4. Crie uma função para solicitar 3 produtos e os respectivos preços. Ao final, mostre a relação de cada

# produto com o respectivo preço.

# 5. Crie uma função para solicitar a figura geométrica (circulo, triangulo e retângulo). Após isso, solicite

# ao usuário as respectivas dimensões para calcular a área.


