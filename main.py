import os
import pandas as pd
import plotly.express as px

# Listar os arquivos no diretório de vendas
caminho_diretorio = "C:\\Users\\Rosiana Engel\\Desktop\\ProjetoPythonRelatorio\\Vendas"
lista_arquivos = os.listdir(caminho_diretorio)

# Inicializar um DataFrame vazio para armazenar os dados de todos os arquivos
tabela_total = pd.DataFrame()

# Iterar sobre os arquivos no diretório
for arquivo in lista_arquivos:
    if "Vendas" in arquivo:
        caminho_arquivo = os.path.join(caminho_diretorio, arquivo)  # Construir o caminho completo para o arquivo
        tabela = pd.read_csv(caminho_arquivo)  # Ler o arquivo CSV
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)  # Concatenar DataFrames

# Calcular o faturamento
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Preco Unitario', 'Faturamento']].sort_values(by='Faturamento', ascending=False)

# Calcular a loja que mais vendeu
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]

# Criar um gráfico de barras para o faturamento por loja
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento', title="Faturamento por Loja")
grafico.show()