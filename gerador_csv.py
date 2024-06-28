import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

# Definindo o ano desejado
ano_desejado = 2023

# Gerando dados simulados
np.random.seed(0)  # Para garantir a reprodutibilidade dos resultados

# Criando dados para 1000 registros
num_registros = 10000

# Função para gerar datas aleatórias dentro do ano
def gerar_datas_aleatorias(num_registros, ano):
    datas = []
    inicio_ano = date(ano, 1, 1)
    fim_ano = date(ano, 12, 31)
    delta = fim_ano - inicio_ano
    
    for _ in range(num_registros):
        dias_passados = random.randint(0, delta.days)
        data = inicio_ano + timedelta(days=dias_passados)
        datas.append(data)
    
    return datas

# Gerando dados simulados para cada registro
datas = gerar_datas_aleatorias(num_registros, ano_desejado)
vendas = np.random.randint(100, 1000, size=num_registros)  # Número de vendas mensais
receita = vendas * np.random.uniform(50, 150, size=num_registros)  # Receita gerada
custos = receita * np.random.uniform(0.1, 0.3, size=num_registros)  # Custos associados

# Criando DataFrame
dados = pd.DataFrame({
    'datas': datas,
    'Vendas': vendas,
    'Receita': receita,
    'Custos': custos
})

# Salvando os dados em um arquivo CSV
dados.to_csv(f'dados_vendas_mensais_{ano_desejado}.csv', index=False)
