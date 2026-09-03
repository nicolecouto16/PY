
########################Exercícios sobre função def#########################################



# 1. Crie uma função para transformar temperatura Farh em Celsius.
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

temp_f = float(input("Digite a temperatura em Fahrenheit: "))

# A função recebe o número digitado e faz o cálculo
temp_c = fahrenheit_para_celsius(temp_f)

print(f"{temp_f}°F equivale a {temp_c:.1f}°C")

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
def calcular_media():
    soma = 0

    # O loop executa 5 vezes para pedir cada número
    for i in range(1, 6):
        valor = float(input(f"Digite o {i}º valor: "))
        soma += valor  # Adiciona o valor digitado ao total

    media = soma / 5
    return media

# Executando a função
resultado = calcular_media()
print(f"\nA média dos 5 valores digitados é: {resultado:.2f}")


# 4. Crie uma função para solicitar 3 produtos e os respectivos preços. Ao final, mostre a relação de cada

def cadastrar_produtos():
    produtos = []

    # Solicita 3 produtos e seus preços
    for i in range(1, 4):
        nome = input(f"Digite o nome do {i}º produto: ")
        preco = float(input(f"Digite o preço do {i}º produto (R$): "))
        
        # Guarda as informações juntas em uma lista
        produtos.append({"nome": nome, "preco": preco})

    # Mostra a relação dos produtos digitados
    print("\n--- RELAÇÃO DE PRODUTOS ---")
    for item in produtos:
        print(f"Produto: {item['nome']} | Preço: R$ {item['preco']:.2f}")


# Executando a função
cadastrar_produtos()
# produto com o respectivo preço.

# 5. Crie uma função para solicitar a figura geométrica (circulo, triangulo e retângulo). Após isso, solicite
# ao usuário as respectivas dimensões para calcular a área.

import math

def area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    return math.pi * (raio ** 2)

def area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    return (base * altura) / 2

def area_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    return base * altura

def calcular_area():
    print("Escolha a figura geométrica:")
    print("1 - Círculo")
    print("2 - Triângulo")
    print("3 - Retângulo")
    
    opcao = input("Digite o número ou nome da opção desejada: ").strip().lower()

    if opcao in ["1", "circulo", "círculo"]:
        area = area_circulo()
        print(f"\nA área do círculo é: {area:.2f}")
    elif opcao in ["2", "triangulo", "triângulo"]:
        area = area_triangulo()
        print(f"\nA área do triângulo é: {area:.2f}")
    elif opcao in ["3", "retangulo", "retângulo"]:
        area = area_retangulo()
        print(f"\nA área do retângulo é: {area:.2f}")
    else:
        print("\nOpção inválida! Escolha entre círculo, triângulo ou retângulo.")

# Executando a função principal
calcular_area()