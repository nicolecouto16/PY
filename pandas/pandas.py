
vendedor = ['ana', 'bruno', 'carlos',' pedro']
vendas = [12000, 2000, 15000, 40000]
meta = [10000, 10000, 10000, 10000]

#crie uma estrutura em py utilizando zip, append, for e crie uma nova coluna chamada situação

#se venda >= meta - meta atingida
#se venda < meta - meta da meta

import pandas as pd

dados = {
    'vendedores': ['ana', 'bruno', 'carlos', 'pedro'],
    'venda': [12000, 2000, 15000, 40000],
    'metas': [10000, 10000, 10000, 10000]
}

df = pd.DataFrame({
    'vendedores': ['ana', 'bruno', 'carlos', 'pedro'],
    'venda': [12000, 2000, 15000, 40000],
    'metas': [10000, 10000, 10000, 10000]
})

lista_metas = []

for vendedores, venda, meta in zip(df['vendedores'], df['venda'], df['metas']):
    if venda >= meta:
        lista_metas.append('Meta atingida')
    else:
        lista_metas.append('Abaixo da meta')

df['Status_da_meta'] = lista_metas

print(df)

#####################################################################

sensor = [S1, S2, S3, S4, S5]
temperatura = 45, 76, 78, 109, 33
vibracao = 2.1, 2.4, 4.4, 4.7, 9.9

#Crie uma estrutura em python utilizando zip, for e condição para mostrar se a classificação do sistema está critico, atenção e normal em função da seguinte lógica:

#temperatura > 90 e vibração > 4 - critico
#temperatura > 80 e vibração > 3.5 - atenção
#Qualquer outra condição - normal

import pandas as pd


dados = {
    'sensor': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'temperatura': [45, 76, 78, 109, 33],
    'vibracao': [2.1, 2.4, 4.4, 4.7, 9.9]
}

df = pd.DataFrame({
    'sensor': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'temperatura': [45, 76, 78, 109, 33],
    'vibracao': [2.1, 2.4, 4.4, 3.0, 9.9]
})

lista_sensor = []

for sensor, temperatura, vibracao in zip(df['sensor'], df['temperatura'], df['vibracao']):
    if temperatura > 90 and vibracao < 4:
        lista_sensor.append('critico')
    elif temperatura > 80 and vibracao < 3.5:
        lista_sensor.append('atenção')
    else:
        lista_sensor.append('normal')

df['Status_do_sensor'] = lista_sensor

print(df)
# ____________________________________

# Exercício 3

# Crie uma estrutura para mostrar se existe falha ou não na máquina. Crie a coluna Status da máquina.

# velocidade de rotação entre 1168 e 2695 e torque 12,6 e 70 não há falha. Qualquer outra condição falha na máquina.

# Utilize o dataframe chamado dataset_falhas_maquinas.







