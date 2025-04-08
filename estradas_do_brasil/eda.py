import pandas as pd
from config import dataset

# %% Definindo métodos

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, sep=';')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    
# %% Execução do código

if __name__ == "__main__":

    # importando bases de dados

    pass