import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Obter dados
try:
    os.system("cls")
    print("Obtendo dados...")

    ENDERECO_DADOS="https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"
    
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding="iso-8859-1")

    df_lesoes = df_ocorrencias[["cisp","lesao_corp_dolosa", "lesao_corp_culposa"]]

    df_total_lesoes = df_lesoes.groupby(["cisp"]).sum(["lesao_corp_dolosa","lesao_corp_culposa"]).reset_index()

    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")
    exit()

# CORRELAÇÃO
try:
    print("\nCalculando a correlação...")

    correlacao = np.corrcoef(
        df_total_lesoes["lesao_corp_dolosa"],
        df_total_lesoes["lesao_corp_culposa"])
    
    print(f"\nCorrelação: {correlacao[0,1]}\nCorrelação em matriz:\n{correlacao}")

except ImportError as e:
    print(f"Erro: {e}")

# GRAFICO
try:
    plt.scatter(df_total_lesoes['lesao_corp_dolosa'],df_total_lesoes["lesao_corp_culposa"])
    plt.title(f"Correlação:\n{correlacao}")
    plt.xlabel("Lesão Corporal Dolosa")
    plt.ylabel("Lesão Corporal Culposa")
    plt.show()

except ImportError as e:
    print(f"Erro: {e}")
