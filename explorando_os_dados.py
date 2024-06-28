import pandas as pd

# Carregar os dados do arquivo CSV
arquivo = 'dados_vendas_mensais_2023.csv'
dados = pd.read_csv(arquivo)

# Exibir as primeiras linhas do DataFrame para entender a estrutura dos dados
print(dados.head())

# Informações gerais sobre o DataFrame
print(dados.info())

# Resumo estatístico das variáveis numéricas
print(dados.describe())