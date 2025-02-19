import pandas as pd

def get_first_document(file_path):
    """Lê o primeiro documento da coluna 'DOCUMENTO' no arquivo Excel para testes."""
    try:
        df = pd.read_excel(file_path, engine="openpyxl")  # Garante que lê o arquivo corretamente
        
        # Verifica se a coluna 'DOCUMENTO' existe
        if "DOCUMENTO" not in df.columns:
            raise ValueError("A coluna 'DOCUMENTO' não foi encontrada no arquivo Excel.")

        # Obtém o primeiro valor da coluna DOCUMENTO
        first_document = df["DOCUMENTO"].dropna().astype(str).iloc[0]  # Converte para string
        
        print(f"Documento encontrado para teste: {first_document}")  # Confirma o valor no terminal
        return first_document
    
    except IndexError:
        print("Erro: O arquivo Excel está vazio ou sem valores na coluna 'DOCUMENTO'.")
        return None
    
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None
