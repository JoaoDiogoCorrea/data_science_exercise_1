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

# Verificar se há valores faltantes
print("\nValores faltantes por coluna:")
print(dados.isnull().sum())

# Plotar um histograma das vendas mensais
import matplotlib.pyplot as plt
plt.hist(dados['Vendas'], bins=20, edgecolor='black')
plt.title('Distribuição das Vendas Mensais')
plt.xlabel('Vendas')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()