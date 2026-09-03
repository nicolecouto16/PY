
#ex.01
class Estrutura:
    estruturas = []

    def __init__(self, nome, carro, ano, modelo):
        self.nome = nome
        self.carro = carro
        self.ano = ano
        self.modelo = modelo
        Estrutura.estruturas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.carro} | {self.ano} | {self.modelo}'

    def listar_estruturas(self):
        for estrutura in Estrutura.estruturas:
            print(f'{estrutura.nome} | {estrutura.carro} | {estrutura.ano} | {estrutura.modelo}')


estrutura_carro = Estrutura('João', 'Corolla', 1987, 'Xein')

estrutura_carro.listar_estruturas()


#ex.02          
class Matematica:
    matematicas = []

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        Matematica.matematicas.append(self)

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f'{self.base} | {self.altura} | {self.calcular_area()} | {self.calcular_perimetro()}'


matematica = Matematica(10, 5)

print('Área:', matematica.calcular_area())
print('Perímetro:', matematica.calcular_perimetro())

#ex.03
class Calcula:
    calcular = []

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        Calcula.calcular.append(self)

    def calcular_imc(self):
        return self.peso / (self.altura * self.altura)

    def resultado_imc(self):
        imc = self.calcular_imc()
        return f'{self.nome} - {self.peso} - {self.altura} - {imc:.2f}'


pessoa = Calcula('Gabriel', 80, 1.80)

print(f'Seu IMC é: {pessoa.calcular_imc():.2f}')
print(pessoa.resultado_imc())

#ex.04
class Calcula:
    calcular = [
        ('Gabriel', 80, 1.80)
        ('Leticia', 56, 1.66)
        ('Joao', 90, 1.60)
        ('Julia', 56, 1.50)
        ('Marlene', 60, 1.60)]

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        Calcula.calcular.append(self)

    def calcular_imc(self):
        return self.peso / (self.altura * self.altura)

    def resultado_imc(self):
        return self.calcular_imc()

#ex.05
#crie um algoritmo para calcular a area e perimetro de um retangulo utilizando a função class
#dps crie 5 objetos e insira em uma lista de objeto.
#por fim, utilize for para inserir a lista de onjetos em um dicionario

class Calcula:
    calcular = []
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

#LISTA DE OBJ
retangulo1 = Calcula(10, 5)
retangulo2 = Calcula(8, 4)
retangulo3 = Calcula(5, 5)
retangulo4 = Calcula(8, 2)
retangulo5 = Calcula(20, 8)

retangulos = [retangulo1, retangulo2, retangulo3, retangulo4, retangulo5]

dicionario = {}

for i, retangulo in enumerate(retangulos, 1):
    dicionario[f'Retangulo {i}'] = {
        'base': retangulo.base,
        'altura': retangulo.altura,
        'area': retangulo.calcular_area(),
        'perimetro': retangulo.calcular_perimetro()
    }
    
print(dicionario)