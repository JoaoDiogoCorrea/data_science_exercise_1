import pandas as pd
import numpy as np
import random

# Gerando dados simulados
np.random.seed(0)  # Para garantir a reprodutibilidade dos resultados

# Criando dados para 12 meses (janeiro a dezembro)
meses = pd.date_range('2023-01-01', periods=12, freq='M')
vendas = np.random.randint(100, 1000, size=12)  # Número de vendas mensais
receita = vendas * np.random.uniform(50, 150, size=12)  # Receita gerada
custos = receita * np.random.uniform(0.1, 0.3, size=12)  # Custos associados

# Criando DataFrame
dados = pd.DataFrame({
    'Mes': meses,
    'Vendas': vendas,
    'Receita': receita,
    'Custos': custos
})

# Salvando os dados em um arquivo CSV
dados.to_csv('dados_vendas_mensais.csv', index=False)

print("Dados salvos com sucesso em 'dados_vendas_mensais.csv'.")