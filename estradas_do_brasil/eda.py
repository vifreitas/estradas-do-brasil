# %% importando bibliotecas

import pandas as pd
from config import paths
import matplotlib.pyplot as plt
import seaborn as sns

# definindo estilo dos plots do seaborn
sns.set_style("whitegrid")

# %% Definindo métodos
    
def files_in_folder(folder_path:str):
    """
    Função para listar os arquivos em uma pasta
    """
    files = os.listdir(folder_path)
    return files

def concatenar_dados(folder_path:str) -> pd.DataFrame:
    """
    Função para concatenar os dados de todas as bases de dados
    """
    # Listando os arquivos na pasta
    files = files_in_folder(folder_path)

    # Inicializando uma lista para armazenar os DataFrames
    dataframes = []

    # Lendo cada arquivo e adicionando à lista
    for file in files:
        file_path = os.path.join(paths.PATH_RAW, file)
        df = pd.read_csv(file_path, sep=';', encoding='latin1')
        if not df.empty:
            dataframes.append(df)

    # Concatenando todos os DataFrames em um único DataFrame
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    
    return concatenated_df

def grafico_de_linhas(df, x, y, titulo, xlabel, ylabel):
    plt.figure(figsize=(12, 6)) # Define o tamanho da figura para melhor visualização

    ax = sns.lineplot(x=x, y=y, data=df, marker='o', linestyle='-')

    # Customizando o gráfico
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Rotacionar os rótulos do eixo X para melhor legibilidade
    plt.xticks(rotation=45)

    # Ajustar layout para evitar sobreposição
    plt.tight_layout()

    nome_arquivo_saida = 'contagem_ocorrencias_mensal.png'
    plt.savefig(nome_arquivo_saida, dpi=300, bbox_inches='tight')

    plt.show()

# %% Execução do código

if __name__ == "__main__":

    # importando base de dados de 2024
    datatran_df = pd.read_csv(paths.PATH_RAW + 'datatran2024.csv', sep=';', encoding='latin1')

    # qte de linhas e colunas
    print(f"{datatran_df.shape[0]} linhas e {datatran_df.shape[1]} colunas")

    #datatran_df.info()

    for col in datatran_df.columns:
        print(col)

    # explicar o que é cada coluna

    # %% Análise Exploratória

    # Quantidade de acidentes por mês
    datatran_df['mes'] = pd.to_datetime(datatran_df['data_inversa'], format='%Y-%m-%d').dt.month

    contagem_mensal_df = datatran_df.groupby('mes').size()
    contagem_mensal_df = contagem_mensal_df.reset_index()

    # Renomear as colunas para clareza
    contagem_mensal_df.columns = ['mes', 'quantidade']

    # Plot
    grafico_de_linhas(contagem_mensal_df, 'mes', 'quantidade', 'Quantidade de Acidentes por Mês', 'Mês', 'Quantidade')

    # %% Horário dos acidentes
    datatran_df['hora'] = pd.to_datetime(datatran_df['horario'], format='%H:%M').dt.hour
        
