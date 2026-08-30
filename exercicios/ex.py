#crie um algoritmo para slicitar marca de carro, versao do cazrro, ano, cor, ipva pago
#solicit 4 infomaçoes para cada tipo de informação. deixe cada informação em uma sublista
#utilize while ou for pra solicitaras infromções reptidas

marca = []
versao = []
ano = []
cor = []
IPVA = []

for i in range (4):
    print(f"\nCadastro do carro {i+1}")
    versao.append(input("Qual a versão do seu carro?: "))
    marca.append(input("Qual a marca do seu carro?: "))
    ano.append(input("Qual o ano do seu carro?: "))
    ano.append(input("Qual a cor do seu carro?: "))
    IPVA.append(input("O seu IPVA está pago? sim/não: "))

carros = [marca, versao, ano, cor, IPVA]

print("\nInformações cadastradas:")
print("Marcas:", carros[0])
print("Versões:", carros[1])
print("Anos:", carros[2])
print("Cores:", carros[3])
print("IPVA pago:", carros[4])

# ---------------------Exercícios função def ------------------------

# 1. crie uma função para calcular a soma, subtração, multiplicação e divisão para dois números. Retorne as 4 operações na função.
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

 

# 2. crie uma função para transformar temperatura em fahrenheit para grau celsius.

# def celsius(f):

#    calc_celsius = (f - 32) * 5/9

#    return calc_celsius 

# celsius(300)

# 3. crie uma função a qual solicite o tipo de figura geométrica (círculo e retângulo). Após isso, crie um programa para calcular a area da respectiva figura geométrica.

# 4. Crie uma função para calcular a media de 4 notas de um aluno utilizando try/except. Ao final retorne a media deste aluno.

# 5. Crie uma função para solicitar a palavra stop ou continue, caso o usuário digite stop, print("Você deve parar."), caso digite continue, print (você pode continuar.) Se o usuário não digitar nenhuma das duas palavras, a pergunta deve continuar de forma infinita. utilize estrutura com while.
