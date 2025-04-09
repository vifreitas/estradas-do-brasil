# %% importando bibliotecas

import pandas as pd
import os
from config import paths

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

# %% Execução do código

if __name__ == "__main__":

    # importando base de dados de 2024
    raw_df = pd.read_csv(paths.PATH_RAW + 'datatran2024.csv', sep=';', encoding='latin1')

    print(len(raw_df))

    raw_df.head()
# %%
