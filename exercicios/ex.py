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