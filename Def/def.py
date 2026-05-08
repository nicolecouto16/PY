
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

